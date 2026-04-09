from datetime import datetime

from pydantic import AnyHttpUrl
from sqlalchemy import Column, TIMESTAMP, text
from sqlmodel import Field, SQLModel


class UrlCreate(SQLModel):
    long_url: AnyHttpUrl


class Urls(SQLModel, table=True):
    id: int | None = Field(index=True, primary_key=True, nullable=False, default=None)
    short_url: str | None = Field(default=None, unique=True)
    long_url: str = Field(default=None, unique=True)
    created_at: datetime | None = Field(
        default=None,
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    )
