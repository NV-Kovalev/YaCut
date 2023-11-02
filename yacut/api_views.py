from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id
from .validators import api_views_validator


@app.route('/api/id/', methods=['POST'])
def get_short_link():
    """Создание короткой ссылки"""
    # Валидация полученных данных.
    data = request.get_json()
    api_views_validator(data)

    # Получаем короткий id.
    if data.get('custom_id'):
        short_id = data.get('custom_id')
    else:
        short_id = get_unique_short_id()

    # Сохраение данных в БД.
    url = URLMap(original=data['url'], short=f'{short_id}').add_and_commit()

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
