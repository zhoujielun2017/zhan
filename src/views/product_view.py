from flask import Blueprint, render_template, request, session, json
from flasgger import swag_from

from model.product_save import ProductSave
from service import user_service, product_service

product = Blueprint('product', __name__)


@product.route('/<code>')
def detail(code):
    mobile = session.get("mobile")
    user = {'mobile': mobile}
    p = product_service.find_by_code(code)
    return p


@product.route('/products', methods=['POST'])
@swag_from("product_view.yml")
def save():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    mobile = data.get('mobile')
    password = data.get('password')
    if mobile or password:
        return '{"code": "fail", "msg": "Invalid productname/password"}'
    if product_service.find_product(mobile, password):
        return '{"code": "product.exists", "msg": "product exists"}'
    save = ProductSave()
    save.mobile = mobile
    save.password = password
    id = product_service.save(save)
    return '{"code": "success","data":"%s"}' % id.id


@product.route('/products', methods=['PUT'])
def update():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    mobile = str(data['mobile'])
    password = str(data['password'])
    product = {'mobile': mobile, 'password': password}
    id = product_service.save(product)
    return '{"code": "success","data":"%s"}' % id


@product.route('/products', methods=['GET'])
def search():
    id = product_service.page(product)
    return '{"code": "success","data":"%s"}' % id


@product.route('/<id>', methods=['DELETE'])
def delete(id):
    product_service.delete(id)
    return '{"code": "success","data":"%s"}' % id
