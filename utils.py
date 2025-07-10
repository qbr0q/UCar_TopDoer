POSITIVE_KEYWORDS = ['хорош', 'люблю', 'прекрасн', 'отличн', 'супер', 'замечательн']
NEGATIVE_KEYWORDS = ['плохо', 'ненавиж', 'ужасн', 'отстой', 'худш', 'разочаров']


def get_sentiment(
        text: str
) -> str:
    """
    Функция для определения "настроения" отзыва
    :param text: текст отзыва
    :return: определенное алгоритмом настроение
    """
    text = text.lower()

    if any(word in text for word in NEGATIVE_KEYWORDS):
        return "negative"
    elif any(word in text for word in POSITIVE_KEYWORDS):
        return "positive"
    else:
        return "neutral"
