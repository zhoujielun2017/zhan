from flask import Blueprint, render_template, request, session, json, jsonify
from flasgger import swag_from

from model.gift_card_code import GiftCardCode
from model.pagination import Pagination
from model.product_save import ProductSave
from model.result import Result
from service import user_service, product_service, gift_card_service
import flask_excel as excel

gift_card = Blueprint('gift_card', __name__)


@gift_card.route('/gift_cards', methods=['POST'])
@swag_from("yml/gift_cards_view_add.yml")
def save():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    area = data.get('area')
    year = data.get('year')
    unit = data.get('unit')
    print = data.get('print')
    num_start = int(data.get('num_start'))
    num_end = int(data.get('num_end'))
    if area == None or year == None or unit == None or num_start == None or print == None:
        return jsonify(Result().fail(code="param.null", msg="Invalid param"))
    if len(area) != 2 or len(year) != 4 or len(unit) != 2 or len(print) != 2:
        return jsonify(Result().fail(code="param.length", msg="param length error"))
    if num_end-num_start > 1000:
        return jsonify(Result().fail(code="param.range", msg="end - start over 1000"))
    for num in range(int(num_start), int(num_end)):
        code = GiftCardCode()
        code.area = area
        code.year = year
        code.unit = unit
        code.print = print
        code.num = num
        if gift_card_service.find_by_code(code.code()) is None:
            gift_card_service.save(code)
    return jsonify(Result().success())


@gift_card.route('/gift_cards', methods=['PUT'])
@swag_from("yml/gift_cards_view_put.yml")
def update():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    code = str(data['code'])
    password = str(data['password'])
    id = gift_card_service.update_used(code,password)
    return jsonify(Result().success())


@gift_card.route('/gift_cards', methods=['GET'])
@swag_from("yml/gift_cards_view_get.yml")
def search():
    page = request.args.get("page")
    page_size = request.args.get("page_size")
    p = Pagination(page, page_size)
    pros = gift_card_service.page(p)
    return jsonify(Result().success(pros.to_dict))


@gift_card.route('/<id>', methods=['DELETE'])
@swag_from("yml/gift_cards_view_delete.yml")
def delete(id):
    gift_card_service.delete(id)
    return jsonify(Result().success())


@gift_card.route('/export', methods=['GET'])
@swag_from("yml/gift_cards_view_export.yml")
def export():
    page = request.args.get("page")
    page_size = request.args.get("page_size")
    p = Pagination(page, page_size)
    pros = gift_card_service.page(p)
    column_names = ['code', 'password']
    return excel.make_response_from_query_sets(pros.queryset, column_names, "xls")

