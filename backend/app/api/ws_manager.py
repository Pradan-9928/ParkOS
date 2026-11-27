"""Per-process websocket broadcaster scaffold; deploy a Redis pub/sub adapter for replicas."""
class WebSocketManager:
    def __init__(self): self.connections = set()
    async def connect(self, websocket): await websocket.accept(); self.connections.add(websocket)
    def disconnect(self, websocket): self.connections.discard(websocket)
    async def broadcast(self, payload):
        for ws in tuple(self.connections):
            try: await ws.send_json(payload)
            except Exception: self.disconnect(ws)
