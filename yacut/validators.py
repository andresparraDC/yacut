""" Спринт 21 - Проект «сервис YaCut»
Автор   Фредди Андрес Парра Орельяна
        Студент факультета Бэкенд. Когорта 14+

Имя файла: validators.py
 - Документ, описывающий все валидаторы проекта
Функции
 - symbols_validation
Классы
 - Allower
"""
from wtforms.validators import DataRequired, URL, Optional, Length, AnyOf, ValidationError

from .constants import ALLOWED_SYMBOLS

# Переменные локали
DataRequired = DataRequired
URL = URL
Optional = Optional
Length = Length


def symbols_validation(string, exception):
    """
    Проверяет, что каждый символ находится в группе:
    - большие латинские буквы,
    - маленькие латинские буквы,
    - цифры в диапазоне от 0 до 9.
    """
    if isinstance(string, str) and all((symbol in ALLOWED_SYMBOLS) for symbol in string):
        return
    raise exception


class Allower(AnyOf):
    """
    Проверяет допустимость символов.
    """
    def __call__(self, form, field):
        if self.message is None:
            self.message = f'Элемент {field.data}, отсутствующий в {self.values}'
        symbols_validation(
            field.data,
            ValidationError(self.message)
        )


def length_validation(sequence, exception, min=1, max=1):
    try:
        getattr(sequence, '__len__')
    except AttributeError:
        raise AttributeError
    if min <= len(sequence) <= max:
        return
    raise exception
