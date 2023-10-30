from flask import flash, redirect, render_template

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import get_unique_short_id

BASE_URL = 'http://127.0.0.1:5000/'


# Главная страница.
@app.route('/', methods=['GET', 'POST'])
def index_view():

    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        original_link_object = URLMap.query.filter_by(original=original_link).first()
        if original_link_object:
            flash(
                f'К этому URL уже привязана короткая ссылка: '
                f'{BASE_URL}{original_link_object.short}'
            )
            return render_template('index.html', form=form)

        if form.custom_id.data:
            if URLMap.query.filter_by(short=form.custom_id.data).first():
                form.custom_id.errors = (f'Имя {form.custom_id.data} уже занято!',)
                return render_template('index.html', form=form)
            short_link = form.custom_id.data
        else:
            short_link = get_unique_short_id()

        url = URLMap(
            original=original_link,
            short=f'{short_link}',
        )
        db.session.add(url)
        db.session.commit()
        flash(
            f'Новая короткая ссылка готова: '
            f'{BASE_URL}{short_link}'
        )
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirect_view(short):
    redirect_link = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(redirect_link.original)
