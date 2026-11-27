"""Async PostgreSQL pool lifecycle helpers."""
from app.config import settings

pool = None

async def connect():
    global pool
    try:
        import asyncpg
        pool = await asyncpg.create_pool(settings.database_url, min_size=1, max_size=10)
    except Exception:
        pool = None  # API health remains available while database is offline.

async def close():
    if pool:
        await pool.close()
