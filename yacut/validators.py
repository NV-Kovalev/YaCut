from re import match

from settings import CUSTOM_ID_LENGHT
from .error_handlers import InvalidAPIUsage
from .models import URLMap


def api_views_validator(data):
    """Валидатор проверяющий корректность полученных данных"""
    # Проверка наличия нужных ключей.
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')

    # Валидация полученного URL.
    original_link = URLMap.query.filter_by(original=data['url']).first()
    if original_link:
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.')

    # Проверка наличия и валидация полученной короткой ссылки.
    if data.get('custom_id'):
        if len(data['custom_id']) > CUSTOM_ID_LENGHT['max']:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')
        if not match(r'^[A-Za-z0-9_]+$', data['custom_id']):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')
        if URLMap.query.filter_by(short=data['custom_id']).first():
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.')
