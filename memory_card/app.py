from flask import Flask, render_template
from common.libs.UrlManager import UrlManager
from appf import app
from controllers.api import route_api
from controllers.api.getToken import route_getToken
from controllers.web.CardWebController import route_card

# app = Flask(__name__)


app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.register_blueprint(route_api, url_prefix='/api')
app.register_blueprint(route_getToken, url_prefix='/getToken')
app.register_blueprint(route_card, url_prefix='/card')


@app.route('/')
def hello_world():
    return 'hello'
    # return render_template("card/index.html")


if __name__ == '__main__':
    app.run(
        port=443,
        debug=True
    )
