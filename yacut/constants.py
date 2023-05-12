""" Спринт 21 - Проект «сервис YaCut»
Автор   Фредди Андрес Парра Орельяна
        Студент факультета Бэкенд. Когорта 14+

Имя файла: constants.py
 - Файл, описывающий все константы, которые будут использоваться в проекте.
"""
from string import ascii_letters, digits

# Пользовательский вариант короткой ссылки не должен превышать 16 символов.
MAX_LEN_SHORT = 16

# Включает буквы, определённые в константах ascii_uppercase и ascii_lowercase.
# Включает следующие буквы: ABCDEFGHIJKLMNOPQRSTUVWXYZ.
# Включает следующие буквы: abcdefghijklmnopqrstuvwxyz.
# digits (0,1,2,3,4,5,6,7,8,9)
ALLOWED_SYMBOLS = f'{ascii_letters}{digits}'

# Формат для ссылки по умолчанию — шесть случайных символов.
LEN_AUTO_SHORT = 6
