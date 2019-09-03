from flask import Blueprint, render_template, request, session, json
from flasgger import swag_from
from service import user_service, user_service

login = Blueprint('login', __name__)


@login.route('/in', methods=['POST'])
@swag_from("login_view_in.yml")
def login_in():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    mobile = str(data['mobile'])
    password = str(data['password'])
    if mobile == '' or password == '':
        return '{"code": "fail", "msg": "Invalid username/password"}'
    if user_service.find_user(mobile, password):
        session["mobile"] = mobile
        return '{"code": "success"}'
    else:
        return '{"code": "fail", "msg": "user not exists"}'


@login.route('/out', methods=['GET'])
@swag_from("login_view_out.yml")
def login_out():
    session.clear()
    return '{"code": "success"}'