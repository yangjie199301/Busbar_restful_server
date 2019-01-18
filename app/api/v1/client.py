# -*- coding: utf-8 -*-
__author__ = 'Terence Yang'
__time__ = '2019/1/18 18:35'
from flask import request
from app.libs.redprint import Redprint
from app.validators.forms import ClientForm
from app.libs.enums import ClientTypeEnum
from app.models.user import User

api = Redprint('client')

@api.route('/register',methods=['POST'])
def create_client():
    data = request.json
    form = ClientForm(data=data)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
    # request.args.to_dict()
    # 注册 登录
    # 参数 校验 验证表单
    # WTForms 验证表单
    pass

def __register_user_by_email(form):
    User.register_by_email(,form.account.data,form.secret.data)
    pass