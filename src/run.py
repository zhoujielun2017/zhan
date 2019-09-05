from datetime import timedelta

from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
import os
from views import area_view, product_view, sell_view, ord_view, login_view, user_view, gift_card_view
import flask_excel as excel
from views.manager import user

app = Flask(__name__,
            template_folder='./web/templates',
            static_folder='D:/data/static',
            static_url_path='',
            )


Swagger(app)
excel.init_excel(app)
CORS(app, supports_credentials=True)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

app.register_blueprint(sell_view.mod)
app.register_blueprint(user.muser, url_prefix='/manager/user')
app.register_blueprint(user_view.user, url_prefix='/user')
app.register_blueprint(area_view.area, url_prefix='/area')
app.register_blueprint(gift_card_view.gift_card, url_prefix='/gift_card')
app.register_blueprint(login_view.login, url_prefix='/login')
app.register_blueprint(product_view.product, url_prefix='/product')
app.register_blueprint(ord_view.ord, url_prefix='/ord')

@app.after_request
def af_request(resp):
    """
    #请求钩子，在所有的请求发生后执行，加入headers。
    :param resp:
    :return:
    """
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE'
    resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return resp

app.run(debug = True)
