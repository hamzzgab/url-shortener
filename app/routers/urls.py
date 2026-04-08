from fastapi import APIRouter, status, HTTPException

router = APIRouter(prefix='/urls', tags=['urls'])

ENCODED_URL = {}
COUNTER = 0

@router.get('/')
def get_urls():
    return ENCODED_URL


@router.post('/')
def shorten_url(url: str):
    global COUNTER

    if url in ENCODED_URL.keys():
        return HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED, detail='encoding already exists')
    COUNTER += 1
    ENCODED_URL[url] = str(COUNTER)
    return {"encoding": str(COUNTER)}


@router.get('/{code}')
def get_url(_id: str):
    url = None
    for key, val in ENCODED_URL.items():
        print(key, val, _id)
        if val == _id:
            url = key
            break
    if not url:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='url not found')
    return {"url": url}
