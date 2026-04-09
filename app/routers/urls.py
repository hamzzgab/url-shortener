from fastapi import APIRouter, status, HTTPException
from sqlmodel import select, col

from app.database import SessionDep
from app.models import Urls, UrlResponse
from app.utils import Base62

router = APIRouter(prefix='/urls', tags=['urls'])
base_62 = Base62()


@router.get('/', response_model=list[Urls])
def get_urls(session: SessionDep):
    query = select(Urls)
    result = session.exec(query).all()
    if not result:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='no urls')
    return result


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Urls)
def shorten_url(url: Urls, session: SessionDep):
    query = select(Urls).where(col(Urls.long_url) == url.long_url)
    if session.exec(query).all():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='url exists')
    session.add(url)
    session.commit()
    session.refresh(url)

    url_id = session.exec(query).first().id
    url.short_url = base_62.encoder(url_id)
    session.add(url)
    session.commit()
    session.refresh(url)

    return url


@router.get('/{code}', status_code=status.HTTP_200_OK, response_model=UrlResponse)
def get_url(code: str, session: SessionDep):
    query = select(Urls).where(col(Urls.short_url) == code)
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='url not found')
    return result
