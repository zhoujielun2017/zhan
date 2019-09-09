from flask import Blueprint, render_template, request, session, json, jsonify
from flasgger import swag_from

from model.pagination import Pagination
from model.product_save import ProductSave
from model.result import Result
from service import user_service, product_service

product = Blueprint('product', __name__)


@product.route('/<code>')
@swag_from("yml/product_view_code.yml")
def detail(code):
    p = product_service.find_by_code(code)
    if p == None:
        return jsonify(Result().fail(code="not.exists", msg="not.exists"))
    return jsonify(Result().success(p.to_dict()))


@product.route('/products', methods=['POST'])
@swag_from("yml/product_view_save.yml")
def save():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    title = data.get('title')
    content = data.get('content')
    main_pic = data.get('main_pic')
    pics = data.get('pics')
    if title == None or content == None:
        return jsonify(Result().fail("param.none", "param.none"))
    save = ProductSave()
    save.title = title
    save.content = content
    save.main_pic = main_pic
    save.pics = pics
    id = product_service.save(save)
    return jsonify(Result().success(id.code))


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
@swag_from("yml/product_view_get.yml")
def search():
    page = request.args.get("page")
    page_size = request.args.get("page_size")
    p = Pagination(page, page_size)
    id = product_service.page(p)
    return jsonify(Result().success(id.to_dict()))


@product.route('/<id>', methods=['DELETE'])
def delete(id):
    product_service.delete(id)
    return jsonify(Result().success())
