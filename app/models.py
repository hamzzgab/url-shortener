from sqlmodel import Field, SQLModel


class Urls(SQLModel, table=True):
    id: int | None = Field(index=True, primary_key=True, nullable=False, default=None)
    short_url: int = Field(unique=True)
    long_url: str


class UrlBase(SQLModel):
    id: int
    short_url: int
    long_url: str

class UrlResponse(SQLModel):
    long_url: str
