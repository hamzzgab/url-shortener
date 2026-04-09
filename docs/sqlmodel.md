# SQLModel in url-shortener

SQLModel combines SQLAlchemy (ORM) and Pydantic (validation) in one class.

---

## Models

### `Urls` — database table

```python
class Urls(SQLModel, table=True):
    id:         int | None = Field(primary_key=True, default=None)
    short_url:  str | None = Field(default=None, unique=True)
    long_url:   str        = Field(default=None, unique=True)
    created_at: datetime | None = Field(
        sa_column=Column(TIMESTAMP(timezone=True), server_default=text("CURRENT_TIMESTAMP"))
    )
```

- `table=True` tells SQLModel to create an actual DB table.
- `id` is auto-assigned by PostgreSQL; `default=None` lets it start as `None` before insertion.
- `created_at` is set by the database, not Python — no need to pass it manually.

### `UrlCreate` — request schema only

```python
class UrlCreate(SQLModel):
    long_url: AnyHttpUrl
```

No `table=True` — this is a Pydantic model used only to validate incoming POST bodies. It enforces that `long_url` is a valid URL with a scheme (`https://...`).

---

## Session

```python
def get_session():
    with Session(engine) as session:
        yield session
```

The session is opened per-request and closed automatically. Injected into routes via `Depends`.

---

## Insert Pattern (two-phase)

Short URLs are Base62-encoded from the DB-generated `id`. Since the `id` only exists after the first commit, insertion requires two steps:

```python
# Step 1 — insert to get the auto-generated id
db_url = Urls(long_url=long_url_str)
session.add(db_url)
session.commit()
session.refresh(db_url)  # db_url.id is now populated

# Step 2 — encode id into short_url and save
db_url.short_url = base62.encoder(db_url.id)
session.add(db_url)
session.commit()
session.refresh(db_url)
```

---

## Query Patterns

```python
# All rows with pagination
select(Urls).limit(limit).offset(skip)

# Find by long_url (duplicate check)
select(Urls).where(col(Urls.long_url) == long_url_str)

# Find by short code
select(Urls).where(col(Urls.short_url) == code)

# Execute
session.exec(query).all()   # returns list
session.exec(query).first() # returns one or None
```
