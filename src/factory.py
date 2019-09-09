import yaml
import os
from flask import Flask

def create_app(config_path=None):
    # 读取配置文件
    if not config_path:
        pwd = os.getcwd()
        config_path = os.path.join(pwd, 'config.yaml')
    conf = read_yaml(config_path)
    print("STATIC_FOLDER %s" % conf["STATIC_FOLDER"])
    app = Flask(__name__,
                template_folder='./web/templates',
                static_folder=conf["STATIC_FOLDER"],
                static_url_path='/static',
                )
    app.config.update(conf)
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
