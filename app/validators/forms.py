# -*- coding: utf-8 -*-
__author__ = 'Terence Yang'
__time__ = '2019/1/18 18:40'
from wtforms import Form, StringField, IntegerField,
from wtforms.validators import DataRequired, length,Email
from app.libs.enums import ClientTypeEnum



class ClientForm(Form):
    account = StringField(validators=[DataRequired(), length(
        min=5,max=32
    )])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])


    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e


class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='invalidate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$')
    ])
    nickname = StringField(validators=[DataRequired(),
                                       length(min=2,max=22)])
    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError()
        pass
