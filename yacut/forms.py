from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class URLForm(FlaskForm):
    original_link = StringField(
        'Динная ссылка',
        validators=[DataRequired(message='Обязательное поле')]
    )
    custom_id = StringField(
        'Вариант короткой ссылки',
        validators=[
            Length(1, 16, message='Ссылка должна быть не больше 16 символов'),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
