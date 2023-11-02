from http import HTTPStatus

from flask import flash, redirect, render_template

from . import app
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id
from settings import BASE_URL


@app.route('/', methods=['GET', 'POST'])
def index_view():
    """Главная страница."""

    # Проверяем получена ли форма.
    form = URLForm()
    if form.validate_on_submit():

        # Валидация оригинальной ссылки.
        if URLMap.query.filter_by(original=form.original_link.data).first():
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('index.html', form=form)

        # Проверка наличия и валидация предложенной короткой ссылки.
        if form.custom_id.data:
            if URLMap.query.filter_by(short=form.custom_id.data).first():
                form.custom_id.errors = (
                    f'Имя {form.custom_id.data} уже занято!',)
                return render_template('index.html', form=form)
            short_id = form.custom_id.data
        else:
            short_id = get_unique_short_id()

        # Сохранение данных в БД.
        URLMap(
            original=form.original_link.data, short=f'{short_id}',
        ).add_and_commit()

        # Возвращаем укороченную ссылку.
        flash(f'{BASE_URL}{short_id}')
        return render_template('index.html', form=form)

    # Если форма не получена, возвращаем главную страницу.
    return render_template('index.html', form=form)


@app.route('/<string:short_id>')
def redirect_view(short_id):
    """Редирект по короткому идентификатору."""

    # Перенаправляем пользователя на оригинальную ссылку.
    redirect_link = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(redirect_link.original, code=HTTPStatus.FOUND)
