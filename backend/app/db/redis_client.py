"""Best-effort Redis connection seam for atomic holds and pub/sub."""
from app.config import settings

client = None

async def connect():
    global client
    try:
        from redis.asyncio import Redis
        client = Redis.from_url(settings.redis_url, decode_responses=True)
        await client.ping()
    except Exception:
        client = None

async def close():
    if client:
        await client.aclose()
