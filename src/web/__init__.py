from datetime import timedelta

from flask import Flask
from flasgger import Swagger
import os
from views import area_view, product_view, sell_view, ord_view

from views.manager import user

app = Flask(__name__)
Swagger(app)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

app.register_blueprint(sell_view.mod)
app.register_blueprint(user.muser, url_prefix='/manager/user')
app.register_blueprint(area_view.area, url_prefix='/base')
app.register_blueprint(product_view.product, url_prefix='/product')
app.register_blueprint(ord_view.ord, url_prefix='/ord')
