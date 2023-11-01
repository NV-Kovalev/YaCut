from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL


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
            Length(1, 16, message='Ссылка должна быть не больше 16 символов'),
            Optional(),
            Regexp(r'^[A-Za-z0-9_]+$', message='Используйте только латинские буквы и цифры')
        ]
    )
    submit = SubmitField('Создать')
