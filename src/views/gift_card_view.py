from json import JSONDecodeError

import flask_excel as excel
from flasgger import swag_from
from flask import Blueprint, request, session, json, jsonify

from model.gift_card_code import GiftCardCode
from model.result import Result
from service import gift_card_service, product_service
from views.util.request_util import RequestUtil

gift_card = Blueprint('gift_card', __name__)


@gift_card.route('/gift_cards', methods=['POST'])
@swag_from("yml/gift_cards_view_add.yml")
def save():
    try:
        data = json.loads(str(request.data, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    area = data.get('area')
    year = data.get('year')
    unit = data.get('unit')
    print1 = data.get('print')
    num_start = int(data.get('num_start'))
    num_end = int(data.get('num_end'))
    if not area or not year or not unit or not num_start or not print1:
        return jsonify(Result().fail(code="param.null", msg="Invalid param"))
    if len(area) != 2 or len(year) != 4 or len(unit) != 2 or len(print1) != 2:
        return jsonify(Result().fail(code="param.length", msg="param length error"))
    if num_end - num_start > 1000:
        return jsonify(Result().fail(code="param.range", msg="end - start over 1000"))
    for num in range(int(num_start), int(num_end)):
        code = GiftCardCode()
        code.area = area
        code.year = year
        code.unit = unit
        code.print = print1
        code.num = num
        if gift_card_service.find_by_code(code.code()) is None:
            gift_card_service.save(code)
    return jsonify(Result().success())


# 礼品卡改为已用
@gift_card.route('/gift_cards', methods=['PUT'])
@swag_from("yml/gift_cards_view_put.yml")
def update():
    try:
        data = json.loads(str(request.data, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    code = str(data['code'])
    password = str(data['password'])
    id = gift_card_service.update_used(code, password)
    return jsonify(Result().success())


# 礼品卡绑定用户
@gift_card.route('/user', methods=['PUT'])
@swag_from("yml/gift_cards_view_bind.yml")
def bind_user():
    try:
        data = json.loads(str(request.data, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    code = str(data['code'])
    password = str(data['password'])
    user_id = session.get("user_id")
    id = gift_card_service.update_bind_user(code, password, user_id)
    return jsonify(Result().success())


# 礼品卡绑定商品
@gift_card.route('/product', methods=['PUT'])
@swag_from("yml/gift_cards_view_product.yml")
def bind_product():
    try:
        data = json.loads(str(request.data, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    product_id = str(data['product_id'])
    codes = data['codes']
    p = product_service.find_by_id(product_id)
    if not p:
        return jsonify(Result().fail(code="product.not.found"))
    gift_card_service.update_bind_product(codes, product_id)
    return jsonify(Result().success())


# 礼品卡绑定商品
@gift_card.route('/product/range', methods=['PUT'])
@swag_from("yml/gift_cards_view_product_range.yml")
def bind_product_range():
    try:
        data = json.loads(str(request.data, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    product_id = str(data['product_id'])
    start_code = data['start_code']
    end_code = data['end_code']
    code = start_code[:-6]
    num_start = int(start_code[-6:])
    num_end = int(end_code[-6:])
    # 0120190101000011
    p = product_service.find_by_id(product_id)
    if not p:
        return jsonify(Result().fail(code="product.not.found"))
    if num_end - num_start > 1000:
        return jsonify(Result().fail(code="param.range", msg="end - start over 1000"))
    codes = []
    for num in range(int(num_start), int(num_end)):
        codes.append(code + str(num).zfill(6))
    gift_card_service.update_bind_product(codes, product_id)
    return jsonify(Result().success())


@gift_card.route('/gift_cards', methods=['GET'])
@swag_from("yml/gift_cards_view_get.yml")
def search():
    status = request.args.get("status")
    p = RequestUtil.get_pagination(request)
    pros = gift_card_service.page(p, status=status)
    return jsonify(Result().success(pros.to_dict()))


@gift_card.route('/<code>', methods=['GET'])
@swag_from("yml/gift_cards_view_code.yml")
def find_by_code(code):
    gift = gift_card_service.find_by_code(code)
    if not gift:
        return jsonify(Result().fail(code="gift_card.not.found"))
    pro = product_service.find_by_id(gift.product_id)
    if not pro:
        return jsonify(Result().fail(code="product.not.bind"))
    return jsonify(Result().success({"gift_card": gift.to_dict(), "product": pro.to_dict()}))


@gift_card.route('/<gid>', methods=['DELETE'])
@swag_from("yml/gift_cards_view_delete.yml")
def delete(gid):
    gift_card_service.delete(gid)
    return jsonify(Result().success())


@gift_card.route('/export', methods=['GET'])
@swag_from("yml/gift_cards_view_export.yml")
def export():
    p = RequestUtil.get_pagination(request)
    pros = gift_card_service.page(p)
    column_names = ['code', 'password', 'product_id', 'status']
    return excel.make_response_from_query_sets(pros.queryset, column_names, "xls")
