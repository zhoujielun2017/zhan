from flask import Blueprint,render_template,request

from service.user_service import find_user

mod = Blueprint('general', __name__)


@mod.route('/sell/')
@mod.route('/sell/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("sell/login.html",user = user)


@mod.route('/sell/login', methods=['GET','POST'])
def login():
    error = None
    mobile = request.form['mobile']
    password = request.form['password']
    if( mobile == '' or password == '' ):
        error = 'Invalid username/password'
        return render_template("sell/login.html", error=error)
    if find_user(mobile,password):
        return render_template("sell/exchange.html", user={ 'mobile': mobile})
    else:
        error = 'Invalid username/password'
    return render_template("sell/login.html",error=error)


@mod.route('/sell/exchange', methods=['POST'])
def exchange():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("sell/exchange.html",user = user)


@mod.route('/sell/createOrd', methods=['GET'])
def createOrd():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("sell/createOrd.html",user = user)


@mod.route('/sell/createOrd', methods=['POST'])
def result():
    user = { 'nickname': 'Miguel' } # fake user
    return render_template("sell/result.html",user = user)
