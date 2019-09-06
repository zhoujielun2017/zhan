import yaml
import os
from flask import Flask

def create_app(config_name=None, config_path=None):

    # 读取配置文件
    if not config_path:
        pwd = os.getcwd()
        config_path = os.path.join(pwd, 'config.yaml')
    if not config_name:
        config_name = 'PRODUCTION'
    conf = read_yaml(config_name, config_path)
    print("STATIC_FOLDER %s" % conf["STATIC_FOLDER"])
    app = Flask(__name__,
                template_folder='./web/templates',
                static_folder=conf["STATIC_FOLDER"],
                static_url_path='/static',
                )
    app.config.update(conf)
    return app


def read_yaml(config_name, config_path):
    """
    config_name:需要读取的配置内容
    config_path:配置文件路径
    """
    if config_name and config_path:
        with open(config_path, 'r', encoding='utf-8') as f:
            conf = yaml.safe_load(f.read())
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            raise KeyError('未找到对应的配置信息')
    else:
        raise ValueError('请输入正确的配置名称或配置文件路径')
