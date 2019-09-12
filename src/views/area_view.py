from flasgger import swag_from
from flask import Blueprint, Response

import service.division_service as division_service

area = Blueprint('area', __name__)


@area.route('/areas', methods=['GET'])
@swag_from("yml/area.yml")
def index():
    return Response(division_service.read(), content_type='application/json')
