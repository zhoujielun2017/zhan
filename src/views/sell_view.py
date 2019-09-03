from flask import Blueprint, render_template, request, session, json
from flasgger import swag_from
from service import user_service

mod = Blueprint('general', __name__)


@mod.route('/sell/')
@mod.route('/sell/index')
def index():
    user = {'nickname': 'Miguel'}  
    return render_template("sell/login.html", user=user)


@mod.route('/sell/login', methods=['POST'])
@swag_from("sell_login.yml")
def login():
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


@mod.route('/sell/createOrd', methods=['GET'])
def createOrd():
    pid = request.form['pid']
    return render_template("sell/createOrd.html", user={})


@mod.route('/sell/createOrd', methods=['POST'])
def result():
    user = {'nickname': 'Miguel'}  
    return render_template("sell/result.html", user=user)
