"""Optional YOLO adapter. Install model/runtime separately on the edge device."""
class BayDetector:
    def __init__(self, model=None): self.model = model
    def classify(self, frame, polygons):
        if self.model is None: return {slot: {"state": "uncertain", "confidence": 0.0} for slot in polygons}
        detections = self.model(frame)
        return {slot: {"state": "uncertain", "confidence": 0.0, "detections": len(detections)} for slot in polygons}
