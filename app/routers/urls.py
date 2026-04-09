from fastapi import APIRouter, status, HTTPException
from fastapi.responses import RedirectResponse
from sqlmodel import select, col

from app.database import SessionDep
from app.models import Urls, UrlCreate
from app.utils import Base62

router = APIRouter(prefix='/urls', tags=['urls'])
base_62 = Base62()


@router.get('/', response_model=list[Urls])
def get_urls(session: SessionDep):
    query = select(Urls)
    result = session.exec(query).all()
    return result


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=Urls)
def shorten_url(url: UrlCreate, session: SessionDep):
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


@router.get('/{code}', status_code=status.HTTP_301_MOVED_PERMANENTLY)
def get_url(code: str, session: SessionDep):
    query = select(Urls).where(col(Urls.short_url) == code)
    result = session.exec(query).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='url not found')
    return RedirectResponse(url=str(result.long_url), status_code=301)
