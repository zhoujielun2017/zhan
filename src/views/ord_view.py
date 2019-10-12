from json import JSONDecodeError

from flasgger import swag_from
from flask import Blueprint, request, json, jsonify, session, current_app

from model.ord_product import OrdProduct
from model.ord_save import OrdSave
from model.result import Result
from service import ord_service, product_service, gift_card_service
from views.util.request_util import RequestUtil

ord = Blueprint('ord', __name__)


@ord.route('/ords', methods=['POST'])
@swag_from("yml/ord_view_post.yml")
def create():
    user_id = session.get("user_id")
    content = request.data
    try:
        data = json.loads(str(content, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
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
        save.add_product({"id": str(product.id), "num": num, "title": product.title})
    save.areas = areas
    save.name = name
    save.mobile = mobile
    save.address = address
    save.user_id = user_id
    save.status = 1
    id = ord_service.save(save)
    return jsonify(Result().success({"id": id}))


@ord.route('/gift_card', methods=['POST'])
@swag_from("yml/ord_view_gift_card.yml")
def create_gift_card():
    user_id = session.get("user_id")
    content = request.data
    try:
        data = json.loads(str(content, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    code = data.get('code')
    password = data.get('password')
    areas = data.get('areas')
    name = data.get('name')
    mobile = data.get('mobile')
    address = data.get('address')
    save = OrdSave()
    gift = gift_card_service.find_by_code(code)
    if not gift:
        current_app.logger.warn("can not find the gift code: %s" % code)
        return jsonify(Result().fail(code="gift.not.found"))
    if password != gift.password:
        return jsonify(Result().fail(code="gift.password.error"))
    if not gift.product_id:
        return jsonify(Result().fail(code="gift.product.relation", msg="gift card not bind to the product"))
    if gift.status != 1:
        return jsonify(Result().fail(code="gift.card.expire", msg="gift card expire or used"))
    save.gift_card_id = str(gift.id)
    save.gift_card_code = gift.code
    product = product_service.find_by_id(gift.product_id)
    if not product:
        return jsonify(Result().fail(code="product.not.exist", msg="product not exist"))
    gift_card_service.update_used(code, password)
    ord_product = OrdProduct()
    ord_product.product_id = str(product.id)
    ord_product.num = 1
    ord_product.title = product.title
    ord_product.main_pic = product.main_pic
    save.add_product(ord_product)
    save.areas = areas
    save.name = name
    save.mobile = mobile
    save.address = address
    save.user_id = user_id
    save.status = 3
    id = ord_service.save(save)
    return jsonify(Result().success({"id": id}))


@ord.route('/ords', methods=['GET'])
@swag_from("yml/ord_view_get.yml")
def page():
    user_id = RequestUtil.get_user_id(session)
    p = RequestUtil.get_pagination(request)
    id = ord_service.page(p, user_id=user_id)
    return jsonify(Result().success(id))


@ord.route('/<id>', methods=['GET'])
@swag_from("yml/ord_view_detail.yml")
def detail(id):
    user_id = RequestUtil.get_user_id(session)
    detail = ord_service.find_by_id(id)
    if not detail or not detail.get("ord"):
        return jsonify(Result().fail(code="ord.not.exist"))
    if not detail.get("ord").user_id or user_id != detail.get("ord").user_id:
        return jsonify(Result().fail(code="ord.not.yours", msg="ord is not yours"))
    ps = list(map(lambda item: item.to_dict(), list(detail.get("products"))))
    return jsonify(Result().success({"ord": detail.get("ord").to_dict(), "products": ps,
                                     "area": None if not detail.get("area") else detail.get("area").to_dict(),
                                     "gift_card": None if not detail.get("gift_card") else detail.get(
                                         "gift_card").to_dict()}))


@ord.route('/<oid>', methods=['DELETE'])
@swag_from("yml/ord_view_delete.yml")
def delete(oid):
    user_id = RequestUtil.get_user_id(session)
    ord_db = ord_service.find_by_id(oid)
    if not ord_db:
        return jsonify(Result().fail(code="ord.not.exists"))
    if not ord_db['ord'].user_id:
        ord_service.delete(oid)
        return jsonify(Result().success())
    if ord_db['ord'].user_id != user_id:
        return jsonify(Result().fail(code="ord.not.yours"))
    ord_service.delete(oid)
    return jsonify(Result().success())
