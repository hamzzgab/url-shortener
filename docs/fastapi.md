# FastAPI in url-shortener

## App Setup

```python
app = FastAPI(lifespan=lifespan)
```

The `lifespan` context manager runs `create_db_and_tables()` on startup — no migrations needed for development.

---

## Router

All URL endpoints live in `app/routers/urls.py`, mounted with:

```python
app.include_router(urls.router)
# prefix: /urls, tag: urls
```

---

## Dependency Injection

The database session is injected into every route via:

```python
SessionDep = Annotated[Session, Depends(get_session)]
```

`get_session()` opens a session and closes it automatically after the request:

```python
def get_session():
    with Session(engine) as session:
        yield session
```

Routes declare it as a parameter:

```python
def get_urls(limit: int = 10, skip: int = 0, session: SessionDep = Depends(get_session)):
```

---

## Request Validation

`UrlCreate` uses `AnyHttpUrl` to reject anything that isn't a valid URL with a scheme:

```python
class UrlCreate(SQLModel):
    long_url: AnyHttpUrl
```

Sending `"example.com"` or `"not-a-url"` returns a **422 Unprocessable Entity** automatically — no manual validation needed.

---

## Endpoints

| Method | Path | Body | Response |
|--------|------|------|----------|
| `GET` | `/urls/` | — | `list[Urls]` |
| `POST` | `/urls/` | `UrlCreate` | `Urls` |
| `GET` | `/urls/{code}` | — | `UrlCreate` (long_url) |

### Status codes
- `201 Created` — successful POST
- `409 Conflict` — URL already exists
- `404 Not Found` — short code not in DB

---

## Settings

Config is loaded from `.env` via `pydantic-settings`:

```python
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    ...

    class Config:
        env_file = "../.env"


settings = Settings()
```

Used in `database.py` to build the PostgreSQL connection string.
