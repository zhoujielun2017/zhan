from flasgger import swag_from
from flask import Blueprint, request, session, json, jsonify

from model.result import Result
from model.user_save import UserSave
from service import user_service

login = Blueprint('login', __name__)


@login.route('/in', methods=['POST'])
@swag_from("yml/login_view_in.yml")
def login_in():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    mobile = data.get('mobile')
    password = data.get('password')
    if not mobile or not password:
        return jsonify(Result().fail(code="param.null", msg="Invalid username/password"))
    user = user_service.find_by_user(mobile, password)
    if user:
        session["user_id"] = str(user.id)
        session["mobile"] = str(user.mobile)
        return jsonify(Result().success({"id": str(user.id)}))
    else:
        return jsonify(Result().fail(code="user.not.exists", msg="user not exists"))


@login.route('/out', methods=['GET'])
@swag_from("yml/login_view_out.yml")
def login_out():
    session.clear()
    return jsonify(Result().success())


@login.route('/reg', methods=['POST'])
@swag_from("yml/login_view_reg.yml")
def reg():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    mobile = data.get('mobile')
    password = data.get('password')
    if not mobile or not password:
        return jsonify(Result().fail(code="param.null", msg="Invalid username/password"))
    if user_service.find_by_mobile(mobile):
        return jsonify(Result().fail(code="user.exists", msg="user exists"))
    else:
        save = UserSave()
        save.mobile = mobile
        save.password = password
        user_id = user_service.save(save)
        session["user_id"] = str(user_id)
        session["mobile"] = str(mobile)
        return jsonify(Result().success({"id": user_id}))
