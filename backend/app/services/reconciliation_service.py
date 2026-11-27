def reconcile(expected_occupied: bool, camera_occupied: bool, confidence: float, sensor_occupied=None):
    uncertain = confidence < .8
    conflict = sensor_occupied is not None and sensor_occupied != camera_occupied
    mismatch = expected_occupied != camera_occupied or conflict
    return {"mismatch": mismatch, "disputed": mismatch or uncertain, "confidence": confidence, "camera": camera_occupied, "sensor": sensor_occupied}
