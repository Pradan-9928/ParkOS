"""Offline-first sensor event loop scaffold. Hardware adapters are injected per deployment."""
import json, time
from offline_queue import OfflineQueue

class EdgeAgent:
    def __init__(self, queue_path="edge-events.sqlite3", api_url="http://backend:8000"):
        self.queue = OfflineQueue(queue_path); self.api_url = api_url; self.running = False
    def observe(self, slot_id, occupied, confidence=1.0, source="simulated"):
        event = {"slot_id": slot_id, "occupied": bool(occupied), "confidence": float(confidence), "source": source, "timestamp": time.time()}
        self.queue.put(event); return event
    def run(self, poll_seconds=2):
        self.running = True
        while self.running: time.sleep(poll_seconds)

if __name__ == "__main__":
    EdgeAgent().run()
