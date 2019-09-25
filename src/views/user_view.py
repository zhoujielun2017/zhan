from flasgger import swag_from
from flask import Blueprint, request, session, json, jsonify

from model.pagination import Pagination
from model.result import Result
from model.user_save import UserSave
from service import user_service

user = Blueprint('user', __name__)


@user.route('/<id>')
def detail(id):
    mobile = session.get("mobile")
    user = {'mobile': mobile}
    p = user_service.find_by_code(id)
    return jsonify(Result().success())


@user.route('/users', methods=['POST'])
@swag_from("yml/user_view_post.yml")
def save():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    mobile = data.get('mobile')
    password = data.get('password')
    if not mobile or not password:
        return jsonify(Result().fail(code="param.null"))
    if user_service.find_by_user(mobile, password):
        return jsonify(Result().fail(code="user.exists", msg="user exists"))
    save = UserSave()
    save.mobile = mobile
    save.password = password
    id = user_service.save(save)
    return jsonify(Result().success({"id": id}))


@user.route('/users', methods=['PUT'])
@swag_from("yml/user_view_put.yml")
def update():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    mobile = data.get('mobile')
    password = data.get('password')
    if not mobile:
        return '{"code": "param.null", "msg": "Invalid username/password"}'
    if not user_service.find_by_mobile(mobile):
        return '{"code": "user.exists", "msg": "user exists"}'
    save = UserSave()
    save.mobile = mobile
    save.password = password
    id = user_service.update(save)
    return jsonify(Result().success())


@user.route('/users', methods=['GET'])
@swag_from("yml/user_view_get.yml")
def search():
    page = request.args.get("page")
    page_size = request.args.get("page_size")
    mobile = request.args.get("mobile")
    p = Pagination(page, page_size)
    id = user_service.page(p, mobile__contains=mobile)
    # logging.debug("This is a debug log.哈哈")
    # logging.info("This is a info log.")
    # current_app.logger.warning("This is a warning log.")
    # current_app.logger.error("This is a error log.")
    # current_app.logger.critical("This is a critical log.")
    return jsonify(Result().success(id.to_dict()))


@user.route('/<id>', methods=['DELETE'])
def delete(id):
    user_service.delete(id)
    return '{"code": "success","data":"%s"}' % id
