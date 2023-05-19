""" Спринт 21 - Проект «сервис YaCut»
Автор   Фредди Андрес Парра Орельяна
        Студент факультета Бэкенд. Когорта 14+

Имя файла: views.py
 - Документ загружает шаблоны, чтобы пользователь мог взаимодействовать с проектом.
Функции
 - index_view()
 - mapping(short_url)
"""
from http import HTTPStatus
from flask import flash, render_template, abort, redirect

from . import app
from .forms import URLMapForm
from .utils import get_urls_from_map, add_url_map
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """
    Главная страница с формой для генерации коротких ссылокю
    """
    template = 'index.html'
    form = URLMapForm()
    if form.validate_on_submit():
        original, short_url, err_message = get_urls_from_map(form)
        if err_message:
            flash(err_message)
            context = {
                'form': form
            }
            return render_template(
                template_name_or_list=template,
                **context
            )
        if not add_url_map(original, short_url):
            flash('Не удалось создать ссылку')
            context = {
                'form': form
            }
            return render_template(
                template_name_or_list=template,
                **context
            )
        flash('Ваша новая ссылка готова')
        flash(short_url)
    context = {
        'form': form
    }
    return render_template(
        template_name_or_list=template,
        **context
    )


@app.route('/<string:short_url>')
def mapping(short_url):
    """
    Перенаправляет с короткой ссылки на оригинальную.
    """
    original_url = URLMap.query.filter_by(short=short_url).first_or_404()
    return redirect(original_url.original)
