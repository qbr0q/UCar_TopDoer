from sqlmodel import SQLModel, Field, create_engine
from sqlalchemy import Text


class Reviews(SQLModel, table=True):
    """
    Модель отзывов
    """
    id: int = Field(default=None, primary_key=True)
    text: str = Field(sa_column=Text)
    sentiment: str = Field(sa_column=Text)
    created_at: str = Field(sa_column=Text) # чтобы в базу летело непосредственно text, а не varchar (по тз)


engine = create_engine("sqlite:///db/reviews.db")
SQLModel.metadata.create_all(engine)
