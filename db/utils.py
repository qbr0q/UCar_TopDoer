from sqlmodel import Session


def insert_review(record, session: Session):
    """
    Функция для вставки данных в базу
    :param record: элемент класса (модели)
    :param session: подключение к бд
    :return: обновлённый объект после вставки
    """
    session.add(record)
    session.commit()
    session.refresh(record)
    return record
