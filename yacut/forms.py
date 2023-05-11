""" Спринт 21 - Проект «сервис YaCut» 
Автор   Фредди Андрес Парра Орельяна
        Студент факультета Бэкенд. Когорта 14+ 
 
Имя файла: forms.py
 - Модель создана для проекта
Класс: 
 - URLMapForm(FlaskForm). 
"""
from flask_wtf import FlaskForm

from wtforms import URLField, StringField, SubmitField
from .validators import DataRequired, URL, Optional, Length, Allower

from .constants import MAX_LEN_SHORT, ALLOWED_SYMBOLS


class URLMapForm(FlaskForm):
    """
    Форма для работы с моделью URLMap.

    Поля:
    original_link   поле для оригинальной длинной ссылки,
    custom_id       поле для пользовательского варианта короткого идентификатора,
    submit          Кнопка подтверждения.
    """ 
    original_link = URLField(
        'Введите оригинальную ссылку',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Некорректный URL')
        ]
    )
    custom_id = StringField(
        f'Введите название до {MAX_LEN_SHORT} символов',
        validators=[
            Optional(),
            Length(
                max=MAX_LEN_SHORT,
                message='Слишком длинное'
            ),
            Allower(
                values=ALLOWED_SYMBOLS,
                message='Разрешены только латиница и цифры'
            )
        ]
    )
    submit = SubmitField(
        'Создать'
    )
