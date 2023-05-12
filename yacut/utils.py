""" Спринт 21 - Проект «сервис YaCut»
Автор   Фредди Андрес Парра Орельяна
        Студент факультета Бэкенд. Когорта 14+

Имя файла: utils.py
 - Вспомогательные функции для работы с views.py.
Функции
 - get_unique_short_id()
 - short_url_exist()
 - get_urls_from_map()
 - add_url_map()
"""
import random

from . import db
from .constants import ALLOWED_SYMBOLS, LEN_AUTO_SHORT
from .models import URLMap

from sqlalchemy.exc import IntegrityError


def get_unique_short_id(symbols=ALLOWED_SYMBOLS, length=LEN_AUTO_SHORT):
    """
    Алгоритм формирования коротких идентификаторов переменной длины.
    """
    result = [None] * length
    while True:
        for index in range(length):
            result[index] = random.choice(symbols)
        result = ''.join(result)
        if URLMap.query.filter_by(short=result).first():
            continue
        return result


def short_url_exist(short_url):
    """
    Проверка наличия в базе данных.
    """
    return bool(URLMap.query.filter_by(short=short_url).first())


def get_urls_from_map(form):
    """
    Получает и проверяет данные из формы.
    """
    original = form.original_link.data
    short = form.custom_id.data
    err_message = None
    if not short:
        short = get_unique_short_id()
        # Верните исходную ссылку, короткую ссылку и сообщение об ошибке.
        return original, short, err_message
    if short_url_exist(short):
        err_message = f'Имя {short} уже занято!'
        return original, short, err_message
    return original, short, err_message


def add_url_map(original, short):
    url_map = URLMap(
        original=original,
        short=short
    )
    db.session.add(url_map)
    try:
        db.session.commit()
    except IntegrityError:
        return False
    return True
