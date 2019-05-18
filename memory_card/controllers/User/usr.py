from  flask import Blueprint,request,jsonify,make_response,redirect,g
import json
from common.models.Member import Member
from common.libs.UrlManager import UrlManager
route_user = Blueprint('user_page',__name__)
from common.UserService.UserService import UserService
from config.base_setting import AUTH_COOKIE_NAME
from common.libs.helper import ops_render
from config.DB import db
@route_user.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
      return ops_render("user/login.html")
    resp = {'code':200,'msg':'登录成功','data':{}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if login_name is None or len( login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名"
        return jsonify( resp )

    if login_pwd is None or len( login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的密码"
        return jsonify( resp )


    user_info = Member.query.filter_by(nickname = login_name).first()
    if not user_info:
        resp["code"] = -1
        resp["msg"] = "请输入正确的用户名和密码-1"
        return jsonify(resp)
    if user_info.reg_ip != UserService.genePwd( login_pwd,user_info.salt ):
        resp["code"] = -1
        resp["msg"] = "请输入正确的用户名和密码-2"
        return jsonify(resp)

    if user_info.status != 1:
        resp['code']=-1
        resp['msg'] ="账户已经被禁用,请联系管理员处理"
        return jsonify(resp)

    response = make_response(json.dumps(resp))
    response.set_cookie(AUTH_COOKIE_NAME,"%s#%s"%(UserService.geneAuthCode(user_info),user_info.uid))


    return response

@route_user.route("/edit", methods=["GET","POST"])
def edit():
    if request.method == "GET":
        return ops_render("user/edit.html")
    resp = {'code': 200, 'msg': '修改成功', 'data': {}}
    req = request.values
    nickname = req['nickname'] if 'nickname' in req else ''
    email = req['email'] if 'email' in req else ''

    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的姓名"
        return jsonify(resp)

    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的邮箱"
        return jsonify(resp)
    user_info = g.current_user
    user_info.nickname = nickname
    user_info.email = email

    db.session.add(user_info)
    db.session.commit()
    return jsonify(resp)


@route_user.route("/reset-pwd", methods=["GET","POST"])
def resetPwd():
    if request.method == "GET":
        return ops_render("user/reset_pwd.html")

    resp = {'code': 200, 'msg': '修改成功', 'data': {}}
    req = request.values
    old_password = req['old_password'] if 'old_password' in req else ''
    new_password = req['new_password'] if 'new_password' in req else ''

    if old_password is None or len(old_password) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的原密码"
        return jsonify(resp)

    if new_password is None or len(new_password) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的新密码"
        return jsonify(resp)

    if old_password == new_password:
        resp['code'] = -1
        resp['msg'] ="请重修输入一个把，新密码和原密码不能相同"
    user_info = g.current_user
    user_info.login_pwd = UserService.genePwd(new_password,user_info.login_salt)


    db.session.add(user_info)
    db.session.commit()

    response = make_response(json.dumps(resp))
    response.set_cookie(AUTH_COOKIE_NAME,"%s#%s"%(UserService.geneAuthCode(user_info),user_info.uid))


    return response


@route_user.route("/logout")
def logout():
    responce = make_response( redirect(UrlManager.buildUrl("/user/login")))
    responce.delete_cookie(AUTH_COOKIE_NAME)
    return responce
