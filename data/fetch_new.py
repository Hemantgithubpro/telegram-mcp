"""
fetch_new.py — Incremental fetch of new message pages from the Telegram
channel, storing only messages that are newer than the last seen
`message_id` in `sync_state`.

Usage:
  python3 data/fetch_new.py [--page-size=N]
"""

import argparse
import asyncio
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone

# --- import telethon client used by the MCP server --------------------------

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

PROJECT_ROOT = "/Users/hemant/Computing/Projects/Telegram/telegram-mcp"
SESSION_FILE = os.getenv("TELEGRAM_SESSION",
                          os.path.join(PROJECT_ROOT, "telegram_mcp_session.session"))

API_ID   = int(os.getenv("TELEGRAM_API_ID", "0")) or None
API_HASH = os.getenv("TELEGRAM_API_HASH", None)

if not API_ID or not API_HASH:
    print("[fetch] ERROR: set TELEGRAM_API_ID / TELEGRAM_API_HASH env vars (see README or .env).")

from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel

DB_PATH = "/Users/hemant/Computing/Projects/Telegram/telegram-mcp/data/jobs.db"
CHANNEL_ID = -1002715063688
CHANNEL_NAME = "SDE Premium Referrals 2.O"

async def fetch_latest_messages(page_size: int = 20, channel_id: int = CHANNEL_ID):
    """
    Use Telethon to fetch the most-recent `page_size` messages from the channel.

    Returns a list of dicts in the same structure as the MCP helper output, so
    the downstream upsert code stays identical.
    """
    async with TelegramClient(SESSION_FILE, API_ID, API_HASH) as client:
        try:
            entity = await client.get_entity(PeerChannel(channel_id))
        except Exception as exc:
            print(f"[fetch] Could not resolve channel {channel_id}: {exc}")
            return []

        msgs = await client.get_messages(entity, limit=page_size)
        results = []
        for m in msgs:
            results.append({
                "id": m.id,
                "sender": CHANNEL_NAME,
                "date": m.date.isoformat() if m.date else None,
                "sender_id": CHANNEL_ID,
                "text": m.message or "",
                "engagement": {
                    "views": getattr(m, "views", 0) or 0,
                    "forwards": getattr(m, "forwards", 0) or 0,
                },
                "forwarded": None,
            })
        return results


# ---------------------------------------------------------------------------

def upsert_message(conn, msg, channel_id):
    conn.execute(
        """
        INSERT OR IGNORE INTO channel_messages
            (message_id, channel_id, channel_name, date_posted,
             text, views, forwards, is_forwarded,
             forwarded_from_chat_id, forwarded_from_chat_name, forwarded_post_id,
             raw_json, created_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            msg.get("id"),
            channel_id,
            msg.get("sender") or CHANNEL_USERNAMENAME,
            msg.get("date"),
            msg.get("text"),
            msg.get("engagement", {}).get("views", 0),
            msg.get("engagement", {}).get("forwards", 0),
            bool(msg.get("forwarded")),
            (msg.get("forwarded") or {}).get("from_chat_id"),
            (msg.get("forwarded") or {}).get("from_chat"),
            (msg.get("forwarded") or {}).get("channel_post"),
            json.dumps(msg, ensure_ascii=False),
            datetime.now(timezone.utc).isoformat(),
        ),
    )


def last_seen_id(conn, channel_id):
    row = conn.execute(
        "SELECT last_message_id FROM sync_state WHERE channel_id = ?", (channel_id,)
    ).fetchone()
    return row[0] if row else 0


def update_cursor(conn, channel_id, max_id, max_date):
    conn.execute(
        """
        INSERT INTO sync_state (channel_id, last_message_id, last_date_posted, updated_at)
        VALUES (?, ?, ?, datetime('now'))
        ON CONFLICT(channel_id) DO UPDATE SET
            last_message_id = excluded.last_message_id,
            last_date_posted = excluded.last_date_posted,
            updated_at        = datetime('now')
        """,
        (channel_id, max_id, max_date),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-size", type=int, default=20)
    args = parser.parse_args()

    if not API_ID or not API_HASH:
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys = ON")

    cursor = last_seen_id(conn, CHANNEL_ID)
    print(f"[fetch] Last seen message_id: {cursor}")

    new_msgs = asyncio.run(fetch_latest_messages(args.page_size, CHANNEL_ID))
    new_msgs = [m for m in new_msgs if m.get("id") and m["id"] > cursor]

    print(f"[fetch] {len(new_msgs)} new messages since last run.")

    inserted = 0
    for m in new_msgs:
        before = conn.execute("SELECT 1 FROM channel_messages WHERE message_id=?", (m["id"],)).fetchone()
        upsert_message(conn, m, CHANNEL_ID)
        if not before:
            inserted += 1

    if new_msgs:
        max_id  = max(m["id"] for m in new_msgs)
        max_date = max(m["date"] for m in new_msgs if m.get("date"))
        update_cursor(conn, CHANNEL_ID, max_id, max_date)
        conn.commit()
    else:
        conn.commit()

    conn.close()
    print(f"[fetch] Done. {inserted} new rows inserted. Cursor -> id={max_id if new_msgs else cursor}")


if __name__ == "__main__":
    main()
