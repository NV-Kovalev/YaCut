from flask_wtf import FlaskForm
from wtforms import URLField
from wtforms.validators import DataRequired, Length, Optional


class OpinionForm(FlaskForm):
    original_link = URLField(
        'Динная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = URLField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16, message='Ссылка должна быть не больше 16 символов'),
            Optional()
        ]
    )
