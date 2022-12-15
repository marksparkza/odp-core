import json
from typing import Any, Mapping, Optional

from redis import Redis

from odp.config import config


class Cache:
    """Redis-based persistent key-value store."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.redis = Redis(
            host=config.REDIS.HOST,
            port=config.REDIS.PORT,
            db=config.REDIS.DB,
            decode_responses=True,
        )

    def get(self, *keys: str, expire: bool = False) -> Optional[str]:
        """Return a cached string value, optionally expiring it."""
        key = '/'.join(keys)
        value = self.redis.get(f'{self.name}/{key}')
        if expire:
            self.redis.delete(f'{self.name}/{key}')
        return value

    def hget(self, *keys: str, expire: bool = False) -> Optional[dict]:
        """Return a cached dict (hash table), optionally expiring it."""
        key = '/'.join(keys)
        value = self.redis.hgetall(f'{self.name}/{key}')
        if expire:
            self.redis.delete(f'{self.name}/{key}')
        return value

    def jget(self, *keys: str, expire: bool = False) -> Optional[Any]:
        """Deserialize and return a cached JSON object, optionally expiring it."""
        key = '/'.join(keys)
        if jtext := self.redis.get(f'{self.name}/{key}'):
            if expire:
                self.redis.delete(f'{self.name}/{key}')
            return json.loads(jtext)

    def set(self, *keys: str, value: str, expiry: int = None) -> None:
        """Cache a string value, with optional expiry in seconds."""
        key = '/'.join(keys)
        self.redis.set(f'{self.name}/{key}', value, ex=expiry)

    def hset(self, *keys: str, value: Mapping) -> None:
        """Cache a dict (hash table)."""
        key = '/'.join(keys)
        self.redis.hset(f'{self.name}/{key}', mapping=value)

    def jset(self, *keys: str, value: Any, expiry: int = None) -> None:
        """Cache a JSON-serializable object, with optional expiry in seconds."""
        key = '/'.join(keys)
        self.redis.set(f'{self.name}/{key}', json.dumps(value), ex=expiry)
