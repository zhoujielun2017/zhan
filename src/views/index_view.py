from flask import Blueprint, current_app

index = Blueprint('index', __name__)


@index.route('/favicon.ico')
def get_fav():
    return current_app.send_static_file('favicon.ico')
