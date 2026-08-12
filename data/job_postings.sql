-- Raw Telegram messages from the channel
CREATE TABLE IF NOT EXISTS channel_messages (
    message_id INTEGER PRIMARY KEY,        -- Telegram message ID (unique per channel)
    channel_id INTEGER NOT NULL,
    channel_name TEXT NOT NULL,
    date_posted TEXT NOT NULL,              -- ISO timestamp of when the message was POSTED
    text TEXT,                              -- full raw message text
    views INTEGER DEFAULT 0,
    forwards INTEGER DEFAULT 0,
    is_forwarded BOOLEAN DEFAULT 0,
    forwarded_from_chat_id INTEGER,
    forwarded_from_chat_name TEXT,
    forwarded_post_id INTEGER,
    raw_json TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);

-- Parsed / extracted job details with AI analysis
CREATE TABLE IF NOT EXISTS job_postings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id INTEGER NOT NULL,

    -- extracted structured fields (best-effort parsing)
    company TEXT,
    role TEXT,
    batch TEXT,
    ctc TEXT,
    location TEXT,
    apply_link TEXT,
    reference_code TEXT,
    requirements TEXT,
    responsibilities TEXT,
    how_to_apply TEXT,

    -- AI analysis (nullable until generated)
    summary TEXT,
    skill_favor_score  REAL,
    company_reputation INTEGER,
    position_reputation INTEGER,
    analyzed_at TEXT,

    FOREIGN KEY (message_id) REFERENCES channel_messages(message_id) ON DELETE CASCADE
);

-- Tracks last seen message so incremental fetches know where to continue from
CREATE TABLE IF NOT EXISTS sync_state (
    channel_id INTEGER PRIMARY KEY,
    last_message_id INTEGER,
    last_date_posted TEXT,
    updated_at TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_messages_date  ON channel_messages(date_posted);
CREATE INDEX IF NOT EXISTS idx_messages_chan  ON channel_messages(channel_id);
CREATE INDEX IF NOT EXISTS idx_jobs_company   ON job_postings(company);
CREATE INDEX IF NOT EXISTS idx_jobs_role      ON job_postings(role);
CREATE INDEX IF NOT EXISTS idx_jobs_location  ON job_postings(location);
