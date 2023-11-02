import random
import string

from settings import SHORT_ID_GEN_LENGHT
from .models import URLMap


def get_unique_short_id():
    """Функция генерирующая уникальный id для короткой ссылки"""
    short_id = ''.join(
        random.choices(
            string.ascii_letters + string.digits, k=SHORT_ID_GEN_LENGHT)
    )
    if URLMap.query.filter_by(short=short_id).first():
        return get_unique_short_id()
    return short_id
