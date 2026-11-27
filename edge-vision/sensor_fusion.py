def fuse(camera_state, camera_confidence, sensor_state=None):
    if sensor_state is not None and sensor_state == camera_state: return {"state": camera_state, "confidence": max(camera_confidence, .98), "conflict": False}
    if sensor_state is None and camera_confidence >= .8: return {"state": camera_state, "confidence": camera_confidence, "conflict": False}
    return {"state": "uncertain", "confidence": min(camera_confidence, .49), "conflict": sensor_state is not None}
