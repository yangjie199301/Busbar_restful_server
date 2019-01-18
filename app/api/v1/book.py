# -*- coding: utf-8 -*-
__author__ = 'Terence Yang'
__time__ = '2019/1/18 14:54'
from app.libs.redprint import Redprint

# blueprint
# redprint
api = Redprint('book')


@api.route('', methods=['GET'])
def get_book():
    return "我是书"


@api.route('', methods=['POST'])
def create_book():
    return "创建书"
