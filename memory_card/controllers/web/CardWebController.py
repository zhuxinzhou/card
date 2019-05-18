"""
Web页面Controller
只对Web页面的请求做相应的处理
"""

from flask import Blueprint, render_template

from appf import app
from common.libs.helper import ops_render
from common.models.Card import Card

route_card = Blueprint('route_page', __name__)


@route_card.route('/index')
def card_index():
    """
    https://.../card/index
    显示所有信息的主页
    :return:
    """
    view_data = {}

    card_list = Card.query.order_by(Card.id.desc()).all()
    print(type(card_list))
    for test in card_list:
        print(test)
        print(test.id)
        print(test.card_name)

        view_data['card_list'] = card_list
    return ops_render("card/index.html", view_data)
    # return render_template('card/index.html', view_data=view_data)


@route_card.route('/index/today')
def card_index_today():
    pass


@route_card.route('/show')
def card_show():
    pass


@route_card.route('/study')
def card_study():
    pass


@route_card.route('/delete')
def card_delete():
    pass


@route_card.route('/insert')
def card_insert():
    pass
