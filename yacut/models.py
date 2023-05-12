""" Спринт 21 - Проект «сервис YaCut»
Автор   Фредди Андрес Парра Орельяна
        Студент факультета Бэкенд. Когорта 14+

Имя файла: models.py
 - Модель создана для проекта
Класс:
 - URLMap.
"""
from datetime import datetime

from . import db


class URLMap(db.Model):
    """
    Модель для создания таблицы в базе данных.

    Поля:
    id          поле для ID,
    original    поле для оригинальной длинной ссылки,
    short       поле для короткого идентификатора,
    timestamp   поле для временной метки.
    """
    # ID — целое число, первичный ключ
    id = db.Column(db.Integer(), primary_key=True)

    # обязательного для длинной исходной ссылки
    original = db.Column(db.Text(), nullable=False)

    # необязательного для пользовательского варианта короткой ссылки
    # Пользовательский вариант короткой ссылки не должен превышать 16 символов
    short = db.Column(db.String(16), nullable=False, unique=True)

    # Дата и время — текущее время,
    # по этому столбцу база данных будет проиндексирована
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
