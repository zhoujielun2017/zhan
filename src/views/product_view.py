from flask import Blueprint, render_template, request, session, json
from flasgger import swag_from
from service import user_service, product_service

product = Blueprint('product', __name__)


@product.route('/<code>')
def detail(code):
    mobile = session.get("mobile")
    user = {'mobile': mobile}
    p = product_service.find_by_code(code)
    return render_template("product/product.html", user=user,product=p)

