from flask import Blueprint, render_template, request, session, json, jsonify
from flasgger import swag_from

from model.result import Result
from service import user_service, user_service

login = Blueprint('login', __name__)


@login.route('/in', methods=['POST'])
@swag_from("login_view_in.yml")
def login_in():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    mobile = data.get('mobile')
    password = data.get('password')
    if mobile == None or password == None:
        return '{"code": "fail", "msg": "Invalid username/password"}'
    if user_service.find_user(mobile, password):
        session["mobile"] = mobile
        return jsonify(Result().success())
    else:
        return '{"code": "fail", "msg": "user not exists"}'


@login.route('/out', methods=['GET'])
@swag_from("login_view_out.yml")
def login_out():
    session.clear()
    return '{"code": "success"}'
