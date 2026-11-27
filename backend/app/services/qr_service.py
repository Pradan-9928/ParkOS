import base64, hashlib, hmac, json
from app.config import settings

def sign_pass(payload: dict) -> str:
    body = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    sig = hmac.new(settings.hmac_secret.encode(), body, hashlib.sha256).digest()
    return base64.urlsafe_b64encode(body).decode().rstrip("=") + "." + base64.urlsafe_b64encode(sig).decode().rstrip("=")

def verify_pass(token: str) -> dict:
    body64, sig64 = token.split(".", 1)
    body = base64.urlsafe_b64decode(body64 + "=" * (-len(body64) % 4))
    sig = base64.urlsafe_b64decode(sig64 + "=" * (-len(sig64) % 4))
    expected = hmac.new(settings.hmac_secret.encode(), body, hashlib.sha256).digest()
    if not hmac.compare_digest(sig, expected):
        raise ValueError("Invalid pass signature")
    return json.loads(body)
