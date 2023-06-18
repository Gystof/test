from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField
from wtforms.validators import DataRequired
from datetime import datetime
from common.domains import Client


class CreateUpdate(FlaskForm):
    id = IntegerField(label='Идентификатор', default=0)
    email = StringField(label='Почта клиента', validators=[DataRequired()])
    tariff = DateTimeField(label='Название тарифа', validators=[DataRequired()])
    created_at = DateTimeField(label='Дата создания', default=datetime.now())
    

    def __init__(self, storage, *args, **kwargs):
        self.__storage = storage
        super().__init__(*args, **kwargs)

    def save(self) -> bool:
        if not self.validate_on_submit():
            return False
        item = Client(
            id=self.id.data,
            email=self.email.data,
            tariff=self.tariff.data,
            created_at=self.created_at.data
        )
        errors = self.__storage.clients.save(item)
        if not errors:
            return True
        for key, error in errors.items():
            self.__getattribute__(key).errors.append(error)
        return False
