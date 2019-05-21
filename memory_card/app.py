from flask import Flask, render_template, redirect, url_for
from common.libs.UrlManager import UrlManager
from appf import app
from controllers.api import route_api
from controllers.api.getToken import route_getToken
from controllers.web.CardWebController import route_card
from controllers.web.InfoWebController import route_root

app.register_blueprint(route_root, url_prefix='/')
app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.register_blueprint(route_api, url_prefix='/api')
app.register_blueprint(route_getToken, url_prefix='/getToken')
app.register_blueprint(route_card, url_prefix='/card')

if __name__ == '__main__':
    app.run(
        port=443,
        debug=False
    )
