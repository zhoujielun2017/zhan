from flask import Blueprint,render_template,request

from service.user_service import find_user

muser = Blueprint('muser', __name__)


@muser.route('/user/')
@muser.route('/user/index')
def index():

    return render_template("manager/user/user.html")

