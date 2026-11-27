from app.db.redis_client import client

async def hold_slot(lot_id: str, slot_id: str, booking_id: str, ttl_seconds: int = 60) -> bool:
    if client is None: raise RuntimeError("Redis is unavailable; cannot guarantee atomic slot holds")
    key = f"parkos:hold:{lot_id}:{slot_id}"
    return bool(await client.set(key, booking_id, ex=ttl_seconds, nx=True))

async def release_slot(lot_id: str, slot_id: str, booking_id: str) -> bool:
    if client is None: return False
    key = f"parkos:hold:{lot_id}:{slot_id}"
    return bool(await client.eval("if redis.call('get',KEYS[1]) == ARGV[1] then return redis.call('del',KEYS[1]) else return 0 end", 1, key, booking_id))
