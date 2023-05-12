""" Спринт 21 - Проект «сервис YaCut»
Автор   Фредди Андрес Парра Орельяна
        Студент факультета Бэкенд. Когорта 14+

Имя файла: error_handlers.py
 - Обработка ошибок для API проекта.
Классы: 
 - short_url().
 - get_mapping_url() 
"""
from http import HTTPStatus
from flask import jsonify, render_template

from . import app, db


class APIException(Exception):
    """
    Обработчик ошибок для эндпоинтов /api/... .
    """
    def __init__(self, message, status_code=HTTPStatus.BAD_REQUEST):
        super().__init__()
        self.message = message
        self.status_code = status_code
    
    def as_dict(self):
        return dict(message=self.message)


@app.errorhandler(APIException)
def api_exception(error):
    """
    Обрабатывает ошибки для api.
    """
    return jsonify(error.as_dict()), error.status_code


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error):
    """
    Обработчик ошибки 404.
    """
    
    # В качестве ответа возвращается собственный шаблон 
    # и код ошибки
    return render_template('includes/404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error):
    """
    Обработчик ошибки 500.
    """
    
    # В таких случаях можно откатить незафиксированные изменения в БД
    db.session.rollback()
    return render_template('includes/500.html'), HTTPStatus.INTERNAL_SERVER_ERROR
