from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from settings import CUSTOM_ID_LENGHT


class URLForm(FlaskForm):
    """
    Форма для ввода полной и короткой ссылки.
    """

    original_link = URLField(
        'Динная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(require_tld=True, message='Введите URL')
        ]
    )
    custom_id = StringField(
        'Вариант короткой ссылки',
        validators=[
            Length(
                CUSTOM_ID_LENGHT['min'], CUSTOM_ID_LENGHT['max'],
                message=f'Ссылка должна быть не больше '
                        f'{CUSTOM_ID_LENGHT["max"]} символов'
            ),
            Regexp(
                r'^[A-Za-z0-9_]+$',
                message='Используйте только латинские буквы и цифры'),
            Optional(),
        ]
    )
    submit = SubmitField('Создать')
