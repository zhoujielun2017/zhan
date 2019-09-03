from datetime import timedelta

from flask import Flask
from flasgger import Swagger
import os
from views import area_view, product_view, sell_view, ord_view, login_view, user_view

from views.manager import user

app = Flask(__name__,
            template_folder='./web/templates',  # 表示在当前目录 (myproject/A/) 寻找模板文件
            static_folder='./web/static',  # 表示为当前目录 (myproject/A/) 开通虚拟资源入口
            static_url_path='',
            )


Swagger(app)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

app.register_blueprint(sell_view.mod)
app.register_blueprint(user.muser, url_prefix='/manager/user')
app.register_blueprint(user_view.user, url_prefix='/user')
app.register_blueprint(area_view.area, url_prefix='/area')
app.register_blueprint(login_view.login, url_prefix='/login')
app.register_blueprint(product_view.product, url_prefix='/product')
app.register_blueprint(ord_view.ord, url_prefix='/ord')

app.run(debug = True)
