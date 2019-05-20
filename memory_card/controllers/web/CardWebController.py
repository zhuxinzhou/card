"""
Web页面Controller
只对Web页面的请求做相应的处理
"""
import re
import time

from flask import Blueprint, jsonify, request

from common.libs.helper import ops_render, getCurrentDate, iPagination
from common.models.Card import Card
from config.DB import db
from config.base_setting import ONE_PAGE_SHOW, PAGE_DISPLAY

route_card = Blueprint('route_page', __name__)


@route_card.route('/index')
def card_index():
    """
    显示所有信息的主页
    :return: card/index.html view_data
    """
    view_data = {}
    req = request.values
    page_num = int(req['p']) if ('p' in req and req['p']) else 1
    params = {
        'total': Card.query.count(),
        'page_size': ONE_PAGE_SHOW,
        'page': page_num,
        'display': PAGE_DISPLAY,
        'url': request.full_path.replace('&p={}'.format(page_num), "")
    }
    page_set = iPagination(params)
    offset = (page_num - 1) * ONE_PAGE_SHOW

    card_list = Card.query.order_by(Card.id.desc()).offset(offset).limit(ONE_PAGE_SHOW).all()

    view_data['card_list'] = card_list
    view_data['pages'] = page_set
    return ops_render("card/index.html", view_data)
    # return render_template('card/index.html', view_data=view_data)


@route_card.route('/new', methods=['GET'])
def card_new_page():
    """
    到添加界面
    :return: card/set.html
    """
    resp_data = {}
    hour_times = [0 for i in range(24)]
    minute_times = [0 for j in range(60)]
    resp_data['hour_times'] = hour_times
    resp_data['minute_times'] = minute_times
    return ops_render('card/set.html', resp_data)


@route_card.route('/', methods=['POST'])
def card_new():
    """
    添加一条数据
    :return: response 信息
    """
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    req = request.values

    # member_id 无数据库 需要有登录功能后加上
    card_name = req['card_name'] if 'card_name' in req else ''
    card_content = req['card_content'] if 'card_content' in req else ''
    last_time = req['last_time'] if 'last_time' in req else ''

    if len(str(card_name)) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入卡片名称！"
        return jsonify(resp)

    if len(str(card_content)) < 10:
        resp['code'] = -1
        resp['msg'] = "请输入卡片内容，不少于10个字！"
        return jsonify(resp)

    if not time_judge(last_time):
        resp['code'] = -1
        resp['msg'] = "请输入正确的时间！"
        return jsonify(resp)

    new_card = Card()
    # 需要有登录功能后加上
    new_card.member_id = 1
    new_card.card_name = card_name
    new_card.card_content = card_content
    new_card.study_status = 0
    new_card.status = 0
    new_card.created_time = getCurrentDate()
    new_card.last_time = last_time

    try:
        db.session.add(new_card)
        db.session.commit()
        return jsonify(resp)
    except:
        db.session.rollback()
        resp['code'] = -1
        resp['msg'] = "添加失败！"
        return jsonify(resp)


@route_card.route('/<int:card_id>', methods=['DELETE'])
def card_delete(card_id):
    """
    删除 逻辑归档 status = 1
    :param card_id: 本条id
    :return:
    """
    resp = {'code': 200, 'msg': '归档成功', 'data': {}}

    this_card_data = Card.query.filter_by(id=card_id).first()
    if not this_card_data:
        resp['code'] = -1
        resp['msg'] = "错误！"
        return jsonify(resp)

    if this_card_data.status == 1:
        resp['code'] = -1
        resp['msg'] = "该卡片已是归档状态！"
        return jsonify(resp)
    else:
        # status 1 已归档
        this_card_data.status = 1

    this_card_data.last_time = getCurrentDate()

    try:
        db.session.add(this_card_data)
        db.session.commit()
        return jsonify(resp)
    except:
        db.session.rollback()
        resp['code'] = -1
        resp['msg'] = "归档失败！"
        return jsonify(resp)


@route_card.route('/set/<int:card_id>', methods=['GET'])
def card_study(card_id):
    """
    修改页面
    :param card_id: 需要修改的id
    :return: card/set.html
    """
    resp_data = {}
    card_info = Card.query.filter_by(id=card_id).first()
    study_times = [0 for i in range(8)]
    hour_times = [0 for i in range(24)]
    minute_times = [0 for j in range(60)]
    # 2019-05-24 00:00:00
    time_info = str(card_info.last_time)
    time_info_list = re.findall("\\d+", time_info)
    date_info = time_info_list[0] + '-' + time_info_list[1] + '-' + time_info_list[2]
    hour_info = int(time_info_list[3])
    minute_info = int(time_info_list[4])

    resp_data['card_info'] = card_info
    resp_data['hour_times'] = hour_times
    resp_data['minute_times'] = minute_times
    resp_data['study_times'] = study_times
    resp_data['date_info'] = date_info
    resp_data['hour_info'] = hour_info
    resp_data['minute_info'] = minute_info

    return ops_render('card/set.html', resp_data)


@route_card.route('/', methods=['PUT'])
def change_card():
    """
    修改请求
    :return: resp 状态信息
    """
    resp = {'code': 200, 'msg': '操作成功', 'data': {}}
    req = request.values

    # member_id 需要有登录功能后加上
    card_name = req['card_name'] if 'card_name' in req else ''
    card_content = req['card_content'] if 'card_content' in req else ''
    study_status = int(req['study_status']) if 'study_status' in req else -1
    status = int(req['status']) if 'status' in req else -1
    last_time = req['last_time'] if 'last_time' in req else ''

    if len(str(card_name)) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入卡片名称！"
        return jsonify(resp)

    if len(str(card_content)) < 10:
        resp['code'] = -1
        resp['msg'] = "请完善卡片内容，不少于10个字！"
        return jsonify(resp)

    if study_status == -1:
        resp['code'] = -1
        resp['msg'] = "请选择正确学习状态！"
        return jsonify(resp)

    if int(status) not in [0, 1]:
        resp['code'] = -1
        resp['msg'] = "请选择正确的状态数据！"
        return jsonify(resp)

    if not time_judge(last_time):
        resp['code'] = -1
        resp['msg'] = "请输入正确的时间！"
        return jsonify(resp)

    new_card = Card()
    # 需要有登录功能后加上
    new_card.member_id = 1
    new_card.card_name = card_name
    new_card.card_content = card_content
    new_card.study_status = study_status
    new_card.status = status
    new_card.created_time = getCurrentDate()
    new_card.last_time = last_time

    try:
        db.session.add(new_card)
        db.session.commit()
        return jsonify(resp)
    except:
        db.session.rollback()
        resp['code'] = -1
        resp['msg'] = "添加失败！"
        return jsonify(resp)


@route_card.route('/info/<int:card_id>', methods=['GET'])
def show_card_by_id(card_id):
    """
    显示某条详细信息
    :return: card/info.html
    """
    view_data = {}
    this_card_data = Card.query.filter_by(id=card_id).first()
    view_data['this_card_data'] = this_card_data

    return ops_render('card/info.html', view_data)


def time_judge(time_str):
    """
    判断时间过期
    :param time_str:
    :return:
    """
    return time_str > time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
