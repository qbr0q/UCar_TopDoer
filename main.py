from fastapi import FastAPI, Depends
import uvicorn
from sqlmodel import Session, select
from datetime import datetime
from typing import List

from settings import HOST, PORT
from db.models import engine, Reviews
from db.utils import insert_review
from schemas import ReviewIn, ReviewOut
from utils import get_sentiment


app = FastAPI()


def get_session() -> Session:
    """
    Открывает сессию с бд
    :return: сессия с бд
    """
    with Session(engine) as session:
        yield session


@app.post('/reviews', response_model=ReviewOut)
async def send_review(
    json_data: ReviewIn,
    session: Session = Depends(get_session)
) -> Reviews:
    """
    Определяем "настроение" отзыва и записываем в бд
    :param json_data: текст отзыва
    :param session: подключение к бд
    :return: json новой записи в бд
    """
    text = json_data.text
    sentiment = get_sentiment(text)
    created_at = datetime.utcnow().isoformat()

    reviews = Reviews(text=text,
                      sentiment=sentiment,
                      created_at=created_at)
    record = insert_review(reviews, session)
    return record


@app.get('/reviews')
async def get_review(
    sentiment: str,
    session: Session = Depends(get_session)
) -> List[Reviews]:
    """
    Возвращаем массив отзывов, попадающих под фильтрацию
    :param sentiment: фильтр отзывов
    :param session: подключение к бд
    :return: массив отзывов
    """
    stmt = select(Reviews).where(Reviews.sentiment == sentiment)
    records = session.exec(stmt).all()
    return records


if __name__ == "__main__":
    uvicorn.run(
        app,
        host=HOST,
        port=PORT
    )
