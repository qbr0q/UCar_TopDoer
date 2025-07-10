from pydantic import BaseModel


class ReviewIn(BaseModel):
    """
    Модель для описания данные из пост запроса
    """
    text: str


class ReviewOut(BaseModel):
    """
    Модель для структурированного json-ответа (по тз)
    """
    id: int
    text: str
    sentiment: str
    created_at: str
