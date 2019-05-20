from flask import Blueprint, render_template
from werkzeug.utils import redirect

from appf import app
from common.libs.helper import ops_render

route_root = Blueprint('route_root', __name__)


@app.route('/')
def hello_world():
    return redirect('/card/index')


@app.errorhandler(404)
def error_404(error):
    msg = "别乱走"
    return render_template("error/error.html", msg=msg)


@app.errorhandler(405)
def error_404(error):
    msg = "会玩坏"
    return render_template("error/error.html", msg=msg)
