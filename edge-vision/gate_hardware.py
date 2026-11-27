"""Safe hardware boundary. Real relays and cameras must be supplied per site."""
import os
import time
from plate_reader import PlateReader

class GateHardware:
    def __init__(self, plate_reader: PlateReader | None = None):
        self.is_open = False
        threshold = float(os.getenv("ANPR_CONFIDENCE_THRESHOLD", "0.85"))
        self.plate_reader = plate_reader or PlateReader(threshold=threshold)

    def open_barrier(self):
        self.is_open = True
        return {"opened": True, "simulated": True}

    def close_barrier(self):
        self.is_open = False
        return {"opened": False, "simulated": True}

    def scan_qr(self):
        return None  # Inject a site-specific QR scanner adapter.

    def read_plate(self, frame=None, gate="entry"):
        if frame is None:
            return None
        return self.plate_reader.read(frame, gate=gate, captured_at=time.time())
