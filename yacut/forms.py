from flask_wtf import FlaskForm
from wtforms import URLField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Optional, Regexp


class URLForm(FlaskForm):
    original_link = URLField(
        'Введите длинную ссылку',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Проверьте правильность ссылки')]
    )
    custom_id = URLField(
        'Введите ваш вариант короткой ссылки',
        validators=[Optional(),
                    Length(1, 16),
                    Regexp(
                        r'^[A-Za-z0-9]+$',
                        message='Указано недопустимое имя для ссылки')]
    )
    submit = SubmitField('Создать')