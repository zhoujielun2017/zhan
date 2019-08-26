from flask import Blueprint
import json
import service.division_service as division_service

area = Blueprint('base', __name__)


@area.route('/area')
def index():
    return division_service.read()

