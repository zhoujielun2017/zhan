from json import JSONDecodeError

from flasgger import swag_from
from flask import Blueprint, request, json, jsonify, session

from const import const
from model.pagination import Pagination
from model.result import Result
from model.user_adress import UserAddress
from service import user_address_service

user_address = Blueprint('user_address', __name__)


@user_address.route('/<aid>')
@swag_from("yml/user_address_view_detail.yml")
def detail(aid):
    user_id = session.get(const.SESSION_USER_ID)
    ua = user_address_service.find_by_id(aid)
    if ua.user_id != user_id:
        return jsonify(Result().fail(code="error.not.yours"))
    return jsonify(Result().success(ua.to_dict()))


@user_address.route('/address', methods=['POST'])
@swag_from("yml/user_address_view_post.yml")
def save():
    content = request.data
    try:
        data = json.loads(str(content, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    address = UserAddress()
    address.user_id = session.get("user_id")
    get_address_from_json(address, data)
    aid = user_address_service.save(address)
    return jsonify(Result().success({"id": aid}))


@user_address.route('/address', methods=['PUT'])
@swag_from("yml/user_address_view_put.yml")
def update():
    content = request.data
    try:
        data = json.loads(str(content, encoding="utf-8"))
    except JSONDecodeError:
        return jsonify(Result().fail(code="error.json"))
    id = str(data.get("id"))
    address = user_address_service.find_by_id(id)
    if not address:
        return jsonify(Result().fail("address.not.exists"))
    get_address_from_json(address, data)
    user_address_service.update(address)
    return jsonify(Result().success())


def get_address_from_json(address, data):
    address.area1_id = str(data.get("area1_id"))
    address.area2_id = str(data.get("area2_id"))
    address.area3_id = str(data.get("area3_id"))
    address.area1_name = str(data.get("area1_name"))
    address.area2_name = str(data.get("area2_name"))
    address.area3_name = str(data.get("area3_name"))
    address.mobile = str(data.get("mobile"))
    address.address = str(data.get("address"))


@user_address.route('/address', methods=['GET'])
@swag_from("yml/user_address_view_get.yml")
def search():
    page = request.args.get("page")
    page_size = request.args.get("page_size")
    p = Pagination(page, page_size)
    re = user_address_service.page(p)
    return jsonify(Result().success(re.to_dict()))


@user_address.route('/<aid>', methods=['DELETE'])
@swag_from("yml/user_address_view_delete.yml")
def delete(aid):
    user_id = session.get(const.SESSION_USER_ID)
    ua = user_address_service.find_by_id(aid)
    if ua.user_id != user_id:
        return jsonify(Result().fail(code="error.not.yours"))
    if ua:
        user_address_service.delete(aid)
    return jsonify(Result().success())
