# -*- coding: utf-8 -*-
UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'static/upload/',
    'prefix_url':'/static/upload/'
}

APP = {
    'domain':'https://jiyikapian.cn/'
}
domain='https://jiyikapian.cn/'

time_status = [6/12,24,48,72,156,360]

INGNORE_URLS =[
    "^/user/login",
    "/api"

]

INGNORE_CHECK_LOGIN_URLS =[
    "^/static",
    "^/favicon.ico"

]

AUTH_COOKIE_NAME = "Card"