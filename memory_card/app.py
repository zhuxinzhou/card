import re

from flask import Flask, render_template, request, redirect

from common.UrlManager import UrlManager
from common.libs.helper import *

from appf import app
from config.base_setting import INGNORE_URLS, INGNORE_CHECK_LOGIN_URLS, AUTH_COOKIE_NAME
from controllers.User.usr import route_user
from controllers.api import route_api
from controllers.api.getToken import route_getToken
# app = Flask(__name__)


app.register_blueprint(route_user, url_prefix='/user')
app.register_blueprint(route_api,url_prefix='/api')
app.register_blueprint(route_getToken,url_prefix='/getToken')
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.errorhandler(404)
def error_404(e):
    return ops_render('error/error.html', {'status': 404, 'msg': "请抱歉！您访问的页面不存在"})


@app.before_request
def before_request():
    ignore_urls = INGNORE_URLS
    ignore_check_login_urls = INGNORE_CHECK_LOGIN_URLS
    path = request.path
    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
        return
    if"/api" in path:
        return
    user_info = check_login()

    pattern = re.compile('%s' % "|".join(ignore_urls))
    if pattern.match(path):
        return
    if not user_info:
        return redirect(UrlManager.buildUrl("/user/login"))
    if user_info:
        g.current_user = user_info

    LogService.addAccessLog()
    return


def check_login():
    cookies = request.cookies
    auth_cookie = cookies[AUTH_COOKIE_NAME] if AUTH_COOKIE_NAME in cookies else None
    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False
    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()
    except Exception:
        return False
    if user_info is None:
        return False
    if auth_info[0] != UserService.geneAuthCode(user_info):
        return False
    return user_info

if __name__ == '__main__':
    app.run(

      port= 5000,
             debug=True)
