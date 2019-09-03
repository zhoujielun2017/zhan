from flasgger import swag_from
from flask import Blueprint
import service.division_service as division_service

area = Blueprint('area', __name__)


@area.route('/area')
@swag_from("area.yml")
def index():
    return division_service.read()

