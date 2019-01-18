# -*- coding: utf-8 -*-
__author__ = 'Terence Yang'
__time__ = '2019/1/18 14:54'
from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('', methods=['GET'])
def get_user():
    return "我是哈登"


@api.route('', methods=['GET'])
def create_user():
    pass

