import re
from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .views import get_unique_short_id
from .models import URL_map
from .error_handlers import InvalidAPIUsage


@app.route('/api/id/', methods=['POST'])
def add_url():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if 'custom_id' not in data or data['custom_id'] in [None, '']:
        data['custom_id'] = get_unique_short_id()
    if URL_map.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
    if len(data['custom_id']) > 16:
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки'
        )
    if not re.match(r'^[A-Za-z0-9]+$', data['custom_id']):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки'
        )
    url = URL_map()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    url = URL_map.query.filter_by(short=short_id).first()
    if url is not None:
        return jsonify({'url': url.original}), HTTPStatus.OK
    raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
