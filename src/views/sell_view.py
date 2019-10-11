from flask import Blueprint, render_template, request

mod = Blueprint('general', __name__)


@mod.route('/sell/')
@mod.route('/sell/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template("sell/login.html", user=user)


@mod.route('/sell/createOrd', methods=['GET'])
def createOrd():
    pid = request.form['pid']
    return render_template("sell/createOrd.html", user={})


@mod.route('/sell/createOrd', methods=['POST'])
def result():
    user = {'nickname': 'Miguel'}
    return render_template("sell/result.html", user=user)
