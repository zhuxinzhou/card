from flask import Flask,render_template
from common.libs.UrlManager import UrlManager
from appf import app
from controllers.api import route_api
from controllers.api.getToken import route_getToken
# app = Flask(__name__)


app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')
app.add_template_global(UrlManager.buildUrl, 'buildUrl')
app.register_blueprint(route_api,url_prefix='/api')
app.register_blueprint(route_getToken,url_prefix='/getToken')


@app.route('/')
def hello_world():
    return render_template("food/index.html")


if __name__ == '__main__':
    app.run(

      port= 443,
             debug=True)
