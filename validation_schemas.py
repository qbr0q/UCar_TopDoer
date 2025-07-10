from pydantic import BaseModel


class ReviewIn(BaseModel):
    """
    Модель для описания данные из пост запроса
    text - текст отзыва
    """
    text: str


class ReviewOut(BaseModel):
    id: int
    text: str
    sentiment: str
    created_at: str
