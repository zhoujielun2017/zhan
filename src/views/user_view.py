import datetime
from json import JSONDecodeError

from flasgger import swag_from
from flask import Blueprint, request, session, json, jsonify, current_app

from const import const
from model.result import Result
from model.user_save import UserSave
from service import user_service
from views.util.request_util import RequestUtil

user = Blueprint('user', __name__)


@user.route('/<uid>', methods=['GET'])
@swag_from("yml/user_view_detail.yml")
def detail(uid):
    p = user_service.find_by_id(uid)
    if not p:
        return jsonify(Result().fail(code="user.not.exist"))
    return jsonify(Result().success(p.to_dict()))


@user.route('/users', methods=['POST'])
@swag_from("yml/user_view_post.yml")
def save():
    content = request.data
    try:
        data = json.loads(str(content, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    mobile = data.get('mobile')
    password = data.get('password')
    head_url = data.get('head_url')
    if not mobile or not password:
        return jsonify(Result().fail(code="param.null"))
    if user_service.find_by_user(mobile, password):
        return jsonify(Result().fail(code="user.exists", msg="user exists"))
    save = UserSave()
    save.mobile = mobile
    save.password = password
    save.head_url = head_url
    uid = user_service.save(save)
    return jsonify(Result().success({"id": uid}))


@user.route('/users', methods=['PUT'])
@swag_from("yml/user_view_put.yml")
def update():
    try:
        data = json.loads(str(request.data, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    mobile = data.get('mobile')
    password = data.get('password')
    if not mobile:
        return jsonify(Result().fail(code="param.null", msg="Invalid username/password"))
    if not user_service.find_by_mobile(mobile):
        return jsonify(Result().fail(code="user.exists"))
    save = UserSave()
    save.mobile = mobile
    save.password = password
    uid = user_service.update(save)
    return jsonify(Result().success())


@user.route('/password', methods=['PUT'])
@swag_from("yml/user_view_password.yml")
def update_password():
    user_id = session.get(const.SESSION_USER_ID)
    content = request.data
    try:
        data = json.loads(str(content, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    password_old = data.get('password_old')
    password_new1 = data.get('password_new1')
    password_new2 = data.get('password_new2')
    if password_new1 != password_new2:
        return jsonify(Result().fail(code="new_password.not.equal"))
    u = user_service.find_by_id(user_id)
    if password_old != u.password:
        return jsonify(Result().fail(code="old_password.not.equal"))
    u.update(password=str(password_new1), update_time=datetime.datetime.now())
    return jsonify(Result().success())


@user.route('/head', methods=['PUT'])
@swag_from("yml/user_view_head.yml")
def update_head():
    user_id = RequestUtil.get_user_id(session)
    try:
        data = json.loads(str(request.data, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    head = data.get('head_url')
    if not head:
        return jsonify(Result().fail(code="error.head.null"))
    u = user_service.find_by_id(user_id)
    if not u:
        current_app.logger.warn("can not find the user %s" % user_id)
        return jsonify(Result().fail(code="error.not.exists"))
    u.update(head_url=head, update_time=datetime.datetime.now())
    return jsonify(Result().success())


@user.route('/users', methods=['GET'])
@swag_from("yml/user_view_get.yml")
def search():
    p = RequestUtil.get_pagination(request)
    mobile = request.args.get("mobile")
    page = user_service.page(p, mobile__contains=mobile)
    return jsonify(Result().success(page.to_dict()))


@user.route('/<uid>', methods=['DELETE'])
@swag_from("yml/user_view_delete.yml")
def delete(uid):
    user_id = session.get(const.SESSION_USER_ID)
    if user_id == uid:
        return jsonify(Result().fail(code="error.delete.yourself"))
    user_service.delete(uid)
    return jsonify(Result().success())
