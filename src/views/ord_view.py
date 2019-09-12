from flasgger import swag_from
from flask import Blueprint, request, json, jsonify, session

from model.ord_save import OrdSave
from model.pagination import Pagination
from model.result import Result
from service import ord_service, product_service

ord = Blueprint('ord', __name__)


@ord.route('/ords', methods=['POST'])
@swag_from("yml/ord_view_post.yml")
def create():
    user_id = session.get("user_id")
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    pros = data.get('pros')
    areas = data.get('areas')
    name = data.get('name')
    mobile = data.get('mobile')
    address = data.get('address')
    save = OrdSave()
    for pro in pros:
        pid = pro.split("_")[0]
        num = pro.split("_")[1]
        product = product_service.find_by_id(pid)
        if not product:
            return jsonify(Result().fail(code="product.not.exist", msg="product not exist"))
        save.addProduct({"id": str(product.id), "num": num, "title": product.title})
    save.areas = areas
    save.name = name
    save.mobile = mobile
    save.address = address
    save.user_id = user_id
    id = ord_service.save(save)
    return jsonify(Result().success({"id": id}))


@ord.route('/ords', methods=['GET'])
@swag_from("yml/ord_view_get.yml")
def page():
    session.get("user_id")
    page = request.args.get("page")
    page_size = request.args.get("page_size")
    p = Pagination(page, page_size)
    id = ord_service.page(p)
    return jsonify(Result().success(id.to_dict()))


@ord.route('/<id>', methods=['GET'])
@swag_from("yml/ord_view_detail.yml")
def detail(id):
    session.get("user_id")
    ord = ord_service.find_by_id(id)
    return jsonify(Result().success(ord))
