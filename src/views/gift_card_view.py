from flask import Blueprint, render_template, request, session, json
from flasgger import swag_from

from model.gift_card_code import GiftCardCode
from model.pagination import Pagination
from model.product_save import ProductSave
from model.result import Result
from service import user_service, product_service, gift_card_service

gift_card = Blueprint('gift_card', __name__)


@gift_card.route('/gift_cards', methods=['POST'])
@swag_from("gift_cards_view_add.yml")
def save():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    area = data.get('area')
    year = data.get('year')
    unit = data.get('unit')
    print = data.get('print')
    num = data.get('num')
    if area==None or year==None or unit==None or num == None or print == None:
        return Result("param.null", "Invalid param").fail()
    if len(area) !=2 or len(year) != 4 or len(unit) !=2 or len(print) !=2 or len(num) != 6:
        return Result("param.length", "param length error").fail()
    code = GiftCardCode()
    code.area=area
    code.year=year
    code.unit=unit
    code.print=print
    code.num=num
    if gift_card_service.find_by_code(code.code()):
        return Result("gift_card.exists", "gift_card exists").fail()
    id = gift_card_service.save(code)
    return Result().success()


@gift_card.route('/gift_cards', methods=['PUT'])
def update():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    mobile = str(data['mobile'])
    password = str(data['password'])
    gift_card = {'mobile': mobile, 'password': password}
    id = gift_card_service.save(gift_card)
    return '{"code": "success","data":"%s"}' % id


@gift_card.route('/gift_cards', methods=['GET'])
@swag_from("gift_cards_view_get.yml")
def search():
    page = request.args.get("page")
    page_size = request.args.get("page_size")
    p=Pagination(page,page_size)
    pros = gift_card_service.page(p)
    aa = list(map(lambda employee: employee.as_dict(), list(pros)))
    r = Result()
    r.data = aa
    return r.success()


@gift_card.route('/<id>', methods=['DELETE'])
def delete(id):
    gift_card_service.delete(id)
    return '{"code": "success","data":"%s"}' % id
