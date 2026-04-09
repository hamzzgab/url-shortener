# url-shortener

A URL shortener built with FastAPI, PostgreSQL, and Redis.

## Stack

- **FastAPI** — API framework
- **SQLModel** — ORM + request validation
- **PostgreSQL** — persistent storage
- **Redis** — response caching

---

## Setup

### Install dependencies

```bash
pip install -r requirements.txt
```

### Environment variables

Create a `.env` file in the project root:

```
DATABASE_HOSTNAME=
DATABASE_PORT=
DATABASE_PASSWORD=
DATABASE_NAME=
DATABASE_USERNAME=
REDIS_HOST=
REDIS_PORT=
REDIS_DB=
```

### Run

```bash
uvicorn app.main:app --reload
```

Tables are created automatically on startup.

---

## API

### `POST /urls/`

Shorten a URL.

**Body:**
```json
{ "long_url": "https://example.com" }
```

**Returns:** `Urls` object with generated `short_url`.  
**Errors:** `409` if URL already exists, `422` if URL is invalid.

---

### `GET /urls/`

List stored URLs with pagination.

**Query params:** `limit` (default 10), `skip` (default 0)

**Returns:** list of `Urls` objects.

---

### `GET /urls/{code}`

Look up a short code.

**Returns:** `Urls` object.  
**Errors:** `404` if code not found.

---

## Seeding

To populate the database with dummy data:

```bash
pip install faker
python seed.py              # 10 000 rows (default)
python seed.py 1000000000   # 1B rows (uses PostgreSQL COPY for speed)
```
