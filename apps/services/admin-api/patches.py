import redis.asyncio as aioredis
import sys
import fastapi_admin.app

# Monkey patch fastapi_admin to use redis.asyncio instead of aioredis
fastapi_admin.app.Redis = aioredis.Redis
sys.modules['aioredis'] = aioredis 