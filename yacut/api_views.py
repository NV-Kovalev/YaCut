from http import HTTPStatus
from re import match

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def get_short_link():
    """Создание короткой ссылки"""
    data = request.get_json()

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
        if len(data['custom_id']) > 16:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')
        if not match(r'^[A-Za-z0-9_]+$', data['custom_id']):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')
        if URLMap.query.filter_by(short=data['custom_id']).first():
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.')
        short_id = data['custom_id']
    else:
        short_id = get_unique_short_id()

    # Сохраение данных в БД.
    url = URLMap(
        original=data['url'],
        short=f'{short_id}',
    )
    db.session.add(url)
    db.session.commit()

    # Возвращаем укороченную ссылку.
    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    """Получение оригинальной ссылки по короткому идентификатору"""

    # Проверяем наличие ссылки и возвращаем ее.
    redirect = URLMap.query.filter_by(short=short_id).first()
    if redirect:
        return jsonify({'url': f'{redirect.original}'}), HTTPStatus.OK
    raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
