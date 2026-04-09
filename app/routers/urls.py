import json

import redis
from fastapi import APIRouter, status, HTTPException
from sqlmodel import select, col

from app.database import SessionDep
from app.models import Urls, UrlCreate
from app.utils import Base62

TTL = 60 * 3
router = APIRouter(prefix='/urls', tags=['urls'])
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
base_62 = Base62()


@router.get('/', response_model=list[Urls])
def get_urls(limit: int = 10, skip: int = 0, session: SessionDep = None):
    key = f'limit:{limit}/skip:{skip}'
    cache = r.get(key)
    if cache:
        return json.loads(cache)
    query = select(Urls).limit(limit).offset(skip)
    results = session.exec(query).all()
    data = [Urls.model_validate(res).model_dump(mode='json') for res in results]
    r.set(key, json.dumps(data), ex=TTL)
    return results


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Urls)
def shorten_url(url: UrlCreate, session: SessionDep = None):
    long_url_str = str(url.long_url)
    query = select(Urls).where(col(Urls.long_url) == long_url_str)
    if session.exec(query).all():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='url exists')

    db_url = Urls(long_url=long_url_str)
    session.add(db_url)
    session.commit()
    session.refresh(db_url)

    db_url.short_url = base_62.encoder(db_url.id)
    session.add(db_url)
    session.commit()
    session.refresh(db_url)

    return db_url


@router.get('/{code}', status_code=status.HTTP_200_OK, response_model=UrlCreate)
def get_url(code: str, session: SessionDep = None):
    cache = r.get(code)
    if cache:
        return {"long_url": cache}
    query = select(Urls).where(col(Urls.short_url) == code)
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='url not found')
    r.setex(code, TTL, result.long_url)
    return result
