from fastapi import APIRouter, status, HTTPException
from sqlmodel import select, col

from app.database import SessionDep
from app.models import Urls, UrlResponse, UrlBase

router = APIRouter(prefix='/urls', tags=['urls'])


@router.get('/', response_model=list[UrlBase])
def get_urls(session: SessionDep):
    query = select(Urls)
    result = session.exec(query).all()
    if not result:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='no urls')
    return result


@router.get('/{code}', response_model=UrlResponse)
def get_url(code: int, session: SessionDep):
    query = select(Urls).where(col(Urls.short_url) == code)
    result = session.exec(query).one()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='url not found')
    return result


@router.post('/')
def shorten_url(url: str, session: SessionDep):
    global COUNTER

    if url in ENCODED_URL.keys():
        return HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED, detail='encoding already exists')
    COUNTER += 1
    ENCODED_URL[url] = str(COUNTER)
    return {"encoding": str(COUNTER)}
