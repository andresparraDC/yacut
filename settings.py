import os


class Config(object):

    # Подключается БД SQLite
    #SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

    # Задаётся конкретное значение для конфигурационного ключа
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Всесто MY SECRET KEY придумайте и впишите свой ключ
    SECRET_KEY = os.getenv('SECRET_KEY')
