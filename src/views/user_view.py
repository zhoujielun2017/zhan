from flasgger import swag_from
from flask import Blueprint, render_template, request, session, json, jsonify

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
    if mobile or password:
        return '{"code": "fail", "msg": "Invalid username/password"}'
    if user_service.find_user(mobile, password):
        return '{"code": "user.exists", "msg": "user exists"}'
    save = UserSave()
    save.mobile = mobile
    save.password = password
    id = user_service.save(save)
    return jsonify(Result().success())


@user.route('/users', methods=['PUT'])
@swag_from("yml/user_view_put.yml")
def update():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    password = str(data['password'])
    # user = {'mobile': mobile, 'password': password}
    # id = user_service.save(user)
    return jsonify(Result().success())


@user.route('/users', methods=['GET'])
def search():
    id = user_service.page(user)
    return '{"code": "success","data":"%s"}' % id


@user.route('/<id>', methods=['DELETE'])
def delete(id):
    user_service.delete(id)
    return '{"code": "success","data":"%s"}' % id
