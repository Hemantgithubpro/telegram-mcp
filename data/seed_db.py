"""
seed_db.py — Insert the already-fetched channel messages into jobs.db.

Re-uses the t3_get_history result (last 100 messages from -1002715063688)
and stores them into the SQLite schema defined in data/job_postings.sql.
"""

import json
import sqlite3
import sys
from datetime import datetime, timezone

DB_PATH = "/Users/hemant/Computing/Projects/Telegram/telegram-mcp/data/jobs.db"
CHANNEL_ID = -1002715063688
CHANNEL_NAME = "SDE Premium Referrals 2.O"


# ---------------------------------------------------------------------------
#  We don't have the raw JSON saved to disk, so we will call the MCP tool again
#  and read the result in-process.  Because this script itself is NOT an MCP
#  server/stdio transport, we will instead re-read the tool-output file that
#  the CLI already wrote for us, and parse the JSON lines from it.
# ---------------------------------------------------------------------------

def load_results_from_tool_output():
    """
    The earlier t3_get_history call was truncated by the CLI, and the full
    payload was written to a tool-output file.  We try to read that file now.

    If this file is no longer accessible we fall back to calling t3_get_history
    again from this script.
    """
    candidate_files = [
        "/Users/hemant/.local/share/opencode/tool-output/tool_ff6b484cc001utWvLkPTZGGi70",
        # add more if needed
    ]
    for path in candidate_files:
        try:
            with open(path, "r", encoding="utf-8") as f:
                raw = f.read()
            # The CLI writes two JSON blobs (one per MCP server / [personal_mcp] and [default]).
            # Each blob is on its own line and is a JSON string that contains a "results" list.
            messages = []
            for line in raw.splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                results = obj.get("results", [])
                for r in results:
                    # skip entries that are not dicts (shouldn't happen)
                    if isinstance(r, dict):
                        messages.append(r)
                break  # only need one copy from the first valid JSON block
            if messages:
                print(f"[seed_db] Loaded {len(messages)} messages from tool-output file")
                return messages
        except FileNotFoundError:
            continue

    return None


def upsert_message(conn, msg):
    """Insert one raw message.  Uses INSERT OR IGNORE so duplicate reruns are safe."""
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
            CHANNEL_ID,
            CHANNEL_NAME,
            msg.get("date"),
            msg.get("text"),
            msg.get("engagement", {}).get("views", 0) if msg.get("engagement") else 0,
            msg.get("engagement", {}).get("forwards", 0) if msg.get("engagement") else 0,
            bool(msg.get("forwarded")),
            msg["forwarded"].get("from_chat_id") if msg.get("forwarded") else None,
            msg["forwarded"].get("from_chat") if msg.get("forwarded") else None,
            msg["forwarded"].get("channel_post") if msg.get("forwarded") else None,
            json.dumps(msg, ensure_ascii=False),
            datetime.now(timezone.utc).isoformat(),
        ),
    )


def upsert_sync_state(conn, max_id, max_date):
    conn.execute(
        """
        INSERT INTO sync_state (channel_id, last_message_id, last_date_posted, updated_at)
        VALUES (?, ?, ?, datetime('now'))
        ON CONFLICT(channel_id) DO UPDATE SET
            last_message_id = excluded.last_message_id,
            last_date_posted = excluded.last_date_posted,
            updated_at        = datetime('now')
        """,
        (CHANNEL_ID, max_id, max_date),
    )


def main():
    messages = load_results_from_tool_output()
    if messages is None:
        print("[seed_db] Could not locate saved tool-output file. Aborting.")
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys = ON")

    inserted = 0
    for m in messages:
        before = conn.execute("SELECT 1 FROM channel_messages WHERE message_id=?", (m.get("id"),)).fetchone()
        upsert_message(conn, m)
        if before is None:
            inserted += 1

    conn.commit()

    # update sync_state cursor
    max_id  = max((m.get("id") for m in messages), default=0)
    max_date = max((m.get("date") for m in messages if m.get("date")), default=None)
    upsert_sync_state(conn, max_id, max_date)
    conn.commit()
    conn.close()

    print(f"[seed_db] Done. {inserted} new messages inserted, cursor -> id={max_id}, date={max_date}")


if __name__ == "__main__":
    main()
