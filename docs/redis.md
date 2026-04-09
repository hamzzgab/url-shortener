# Redis in url-shortener

Redis is used as a caching layer to avoid hitting PostgreSQL on every request.

## Connection

```python
r = redis.Redis(host=settings.redis_host, port=settings.redis_port, db=settings.redis_db, decode_responses=True)
```

`decode_responses=True` means values come back as strings, not bytes.

---

## Cache Keys

### 1. URL list — `GET /urls/`
**Key:** `limit:{n}/skip:{n}` (e.g. `limit:10/skip:0`)  
**Value:** JSON-serialised list of URL objects  
**TTL:** 3 minutes

```python
cache = r.get(key)
if cache:
    return json.loads(cache)

# cache miss — query DB, store result
r.set(key, json.dumps(data), ex=60 * 3)
```

### 2. Short code lookup — `GET /urls/{code}`
**Key:** the short code (e.g. `1a3B`)  
**Value:** the `long_url` string  
**TTL:** 3 minutes

```python
cache = r.get(code)
if cache:
    return {"long_url": cache}

# cache miss — query DB, store result
r.setex(code, 60 * 3, result.long_url)
```

---

## Flow

```
Request
  └── Redis hit?  ──Yes──> Return cached value
        │
        No
        └── Query PostgreSQL
              └── Store in Redis (TTL 3 min)
                    └── Return result
```

---

## Notes
- Cache is never explicitly invalidated — stale data can exist for up to 3 minutes after a change.
- The list cache (`limit:10/skip:0`) and the code cache are independent; a new URL added via POST does not clear existing list caches.
