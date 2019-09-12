from flasgger import swag_from
from flask import Blueprint, request, json, jsonify

from model.pagination import Pagination
from model.product_save import ProductSave
from model.result import Result
from service import product_service

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
    price = data.get('price')
    pics = data.get('pics')
    if title == None or content == None:
        return jsonify(Result().fail("param.none", "param.none"))
    save = ProductSave()
    save.title = title
    save.content = content
    save.price = price
    save.main_pic = main_pic
    save.pics = pics
    id = product_service.save(save)
    return jsonify(Result().success(id.code))


@product.route('/products', methods=['PUT'])
@swag_from("yml/product_view_update.yml")
def update():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    id = data.get('id')
    title = data.get('title')
    content = data.get('content')
    main_pic = data.get('main_pic')
    price = data.get('price')
    pics = data.get('pics')
    if title == None or content == None:
        return jsonify(Result().fail("param.none", "param.none"))
    save = ProductSave()
    save.id = id
    save.title = title
    save.content = content
    save.price = price
    save.main_pic = main_pic
    save.pics = pics
    id = product_service.update(save)
    return jsonify(Result().success())


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
