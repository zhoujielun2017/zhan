from flasgger import swag_from
from flask import Blueprint, request, json, jsonify

from model.pagination import Pagination
from model.result import Result
from model.user_adress import UserAddress
from service import user_address_service

user_address = Blueprint('user_address', __name__)


@user_address.route('/<id>')
def detail(id):
    p = user_address_service.find_by_id(id)
    return jsonify(Result().success(p.to_dict()))


@user_address.route('/address', methods=['POST'])
@swag_from("yml/user_address_view_post.yml")
def save():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    address = UserAddress()
    address.user_id = data.get("user_id")
    address.area1_id = data.get("area1_id")
    address.area2_id = data.get("area2_id")
    address.area3_id = data.get("area3_id")
    address.area1_name = data.get("area1_name")
    address.area2_name = data.get("area2_name")
    address.area3_name = data.get("area3_name")
    address.name = data.get("area1_name")
    address.mobile = data.get("mobile")
    address.address = data.get("address")
    id = user_address_service.save(address)
    return jsonify(Result().success({"id": id}))


@user_address.route('/users', methods=['PUT'])
@swag_from("yml/user_address_view_put.yml")
def update():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    address = UserAddress()
    address.user_id = data.get("user_id")
    address.area1_id = data.get("area1_id")
    address.area2_id = data.get("area2_id")
    address.area3_id = data.get("area3_id")
    address.area1_name = data.get("area1_name")
    address.area2_name = data.get("area2_name")
    address.area3_name = data.get("area3_name")
    address.name = data.get("area1_name")
    address.mobile = data.get("mobile")
    address.address = data.get("address")
    address.update()
    return jsonify(Result().success())


@user_address.route('/users', methods=['GET'])
@swag_from("yml/user_view_get.yml")
def search():
    page = request.args.get("page")
    page_size = request.args.get("page_size")
    p = Pagination(page, page_size)
    id = user_address_service.page(p)
    return jsonify(Result().success(id.to_dict()))


@user_address.route('/<id>', methods=['DELETE'])
def delete(id):
    user_address_service.delete(id)
    return jsonify(Result().success())