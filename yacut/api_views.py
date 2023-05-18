""" Спринт 21 - Проект «сервис YaCut»
Автор   Фредди Андрес Парра Орельяна
        Студент факультета Бэкенд. Когорта 14+

Имя файла: api_views.py
 - API проекта
Функции:
 - short_url().
 - get_mapping_url()
"""
from http import HTTPStatus
from flask import request, url_for, jsonify
from collections import namedtuple

from . import app
from .error_handlers import APIException
from .validators import length_validation, symbols_validation
from .constants import MAX_LEN_SHORT
from .utils import short_url_exist, get_unique_short_id, add_url_map
from .models import URLMap

from typing import Tuple, Any


URLMap_Fields = namedtuple('Fields', 'id original short timestamp')


@app.route(
    '/api/id/',
    methods=['POST']
)
def short_url() -> Tuple[dict[str, Any], int]:
    """
    POST-запрос на создание новой короткой ссылки.
    """
    data = request.get_json()
    if not data:
        raise APIException('Отсутствует тело запроса')

    APIRequest_Fields = URLMap_Fields(None, 'url', 'custom_id', None)
    original = data.get(APIRequest_Fields.original)
    if original is None:
        raise APIException(f'\"{APIRequest_Fields.original}\" является обязательным полем!')
    short = data.get(APIRequest_Fields.short)
    if short:
        exc = APIException('Указано недопустимое имя для короткой ссылки')  # exception
        length_validation(short, exc, max=MAX_LEN_SHORT)
        symbols_validation(short, exc)
        if short_url_exist(short):
            raise APIException(f'Имя \"{short}\" уже занято.')
    else:
        short = get_unique_short_id()

    add_url_map(original, short)
    APIResponse_Fields = URLMap_Fields(None, 'url', 'short_link', None)
    response = {
        APIResponse_Fields.short: url_for(
            'mapping',
            short_url=short,
            _external=True
        ),
        APIResponse_Fields.original: original
    }
    return jsonify(response), HTTPStatus.CREATED


@app.route(
    '/api/id/<string:short_id>/',
    methods=['GET']
)
def get_mapping_url(short_id) -> Tuple[dict[str, Any], int]:
    """
    GET-запрос на получение оригинальной ссылки
    по указанному короткому идентификатору.
    """
    APIResponse_Fields = URLMap_Fields(None, 'url', 'short_link', None)

    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise APIException('Указанный id не найден', HTTPStatus.NOT_FOUND)
    response = {
        APIResponse_Fields.original: url_map.original
    }
    return response, HTTPStatus.OK
