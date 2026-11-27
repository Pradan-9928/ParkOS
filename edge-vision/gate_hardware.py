class GateHardware:
    """Safe simulation adapter. Replace open_barrier with an approved relay driver."""
    def __init__(self): self.is_open = False
    def open_barrier(self): self.is_open = True; return {"opened": True, "simulated": True}
    def close_barrier(self): self.is_open = False; return {"opened": False, "simulated": True}
    def scan_qr(self): return None
    def read_plate(self): return None
