import sqlite3, hashlib

conn = sqlite3.connect("cache.db")
conn.execute("CREATE TABLE IF NOT EXISTS cache (key TEXT PRIMARY KEY, value TEXT)")

def _key(model, prompt):
    return hashlib.sha256(f"{model}|{prompt}".encode()).hexdigest()

def get(model, prompt):
    row = conn.execute("SELECT value FROM cache WHERE key=?", (_key(model, prompt),)).fetchone()
    return row[0] if row else None

def put(model, prompt, value):
    conn.execute("INSERT OR REPLACE INTO cache VALUES (?,?)", (_key(model, prompt), value))
    conn.commit()