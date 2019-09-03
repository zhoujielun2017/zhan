from flask import Blueprint, render_template, request, session, json
from flasgger import swag_from
from service import user_service, product_service

ord = Blueprint('ord', __name__)


@ord.route('/create', methods=['POST'])
def create():
    mobile = session.get("mobile")
    p_str = request.form["product"]
    code = p_str.split("_")[0]
    user = {'mobile': mobile}
    print(code)
    p = product_service.find_by_code(code)
    return render_template("ord/create.html", user=user,product=p)

