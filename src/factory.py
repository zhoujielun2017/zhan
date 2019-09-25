import logging
import os

import yaml
from flask import Flask

from project import project_dir
from views import area_view, product_view, sell_view, ord_view, login_view, user_view, gift_card_view, file_view, \
    user_address_view
from views.manager import user


def create_app(config_path=None):
    # 读取配置文件
    if not config_path:
        config_path = os.path.join(project_dir, 'config.yaml')
    conf = read_yaml(config_path)
    # print("STATIC_FOLDER %s" % conf["STATIC_FOLDER"])
    app = Flask(__name__,
                template_folder='./web/templates',
                static_folder=conf["STATIC_FOLDER"],
                static_url_path='/static',
                )
    app.config.update(conf)
    log(app)
    blueprint(app)
    return app


def read_yaml(config_path):
    """
    config_path:配置文件路径
    """
    with open(config_path, 'r', encoding='utf-8') as f:
        conf = yaml.safe_load(f.read())
    for config_name in conf.keys():
        conf_dict = conf[config_name.upper()]
        if "CURRENT" in conf_dict.keys():
            return conf[config_name.upper()]
    else:
        raise KeyError('未找到对应的配置信息')


def log(app):
    handler = logging.FileHandler('log.log', encoding='UTF-8')
    handler.setLevel(logging.INFO)
    logging_format = logging.Formatter('%(asctime)s - %(levelname)s -'
                                       ' %(filename)s/%(funcName)s(%(lineno)s) - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)


def blueprint(app):
    app.register_blueprint(sell_view.mod)
    app.register_blueprint(user.muser, url_prefix='/manager/user')
    app.register_blueprint(user_view.user, url_prefix='/user')
    app.register_blueprint(area_view.area, url_prefix='/area')
    app.register_blueprint(file_view.file, url_prefix='/file')
    app.register_blueprint(gift_card_view.gift_card, url_prefix='/gift_card')
    app.register_blueprint(login_view.login, url_prefix='/login')
    app.register_blueprint(product_view.product, url_prefix='/product')
    app.register_blueprint(ord_view.ord, url_prefix='/ord')
    app.register_blueprint(user_address_view.user_address, url_prefix='/address')
