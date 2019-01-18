# -*- coding: utf-8 -*-
__author__ = 'Terence Yang'
__time__ = '2019/1/18 14:42'
from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
