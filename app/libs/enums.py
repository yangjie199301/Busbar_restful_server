# -*- coding: utf-8 -*-
__author__ = 'Terence Yang'
__time__ = '2019/1/18 18:37'
from enum import Enum

class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号
    USER_WX = 201
    pass