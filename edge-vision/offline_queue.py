import json, sqlite3, time

class OfflineQueue:
    def __init__(self, path="edge-events.sqlite3"):
        self.db = sqlite3.connect(path, check_same_thread=False)
        self.db.execute("CREATE TABLE IF NOT EXISTS events (id INTEGER PRIMARY KEY, payload TEXT NOT NULL, created REAL NOT NULL)")
    def put(self, event):
        self.db.execute("INSERT INTO events(payload,created) VALUES (?,?)", (json.dumps(event), time.time())); self.db.commit()
    def pending(self, limit=100):
        return self.db.execute("SELECT id,payload FROM events ORDER BY id LIMIT ?", (limit,)).fetchall()
    def acknowledge(self, event_id):
        self.db.execute("DELETE FROM events WHERE id=?", (event_id,)); self.db.commit()
