from flasgger import swag_from
from flask import Blueprint, request, json, jsonify

from model.ord_save import OrdSave
from model.result import Result
from service import ord_service

ord = Blueprint('ord', __name__)


@ord.route('/ords', methods=['POST'])
@swag_from("yml/ord_view_post.yml")
def create():
    content = request.data
    data = json.loads(str(content, encoding="utf-8"))
    pros = data.get('pros')
    areas = data.get('areas')
    name = data.get('name')
    mobile = data.get('mobile')
    address = data.get('address')
    save = OrdSave()
    save.pros = pros
    save.areas = areas
    save.name = name
    save.mobile = mobile
    save.address = address
    id = ord_service.save(save)
    return jsonify(Result().success({"id": id}))


@ord.route('/ords', methods=['GET'])
@swag_from("yml/ord_view_get.yml")
def list():
    save = OrdSave()
    save.pros = pros
    save.areas = areas
    save.name = name
    save.mobile = mobile
    save.address = address
    id = ord_service.page(save)
    return jsonify(Result().success({"id": id}))
