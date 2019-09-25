import re
from datetime import timedelta

import flask_excel as excel
from flasgger import Swagger
from flask import jsonify, session, request, current_app
from flask_cors import CORS

import factory
from model.result import Result

app = factory.create_app()

Swagger(app)
excel.init_excel(app)
CORS(app, supports_credentials=True)

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.errorhandler(400)
def page_not_found(error):
    return 'param error', 400


@app.errorhandler(500)
def special_exception_handler(error):
    app.logger.error(error)
    return '请联系管理员', 500


@app.before_request
def before_user():
    check_login = current_app.config.get("CHECK_LOGIN")
    testing = current_app.config.get("TESTING")
    if check_login:
        return
    path = request.path
    allow_path = current_app.config.get("ALLOW_NOT_LOGIN")
    for allow in allow_path:
        if re.match(allow, path):
            return
    else:
        if current_app.config.get("TESTING"):
            session["user_id"] = "5d83041c71a281581fe0b93b"
            return
        if not 'user_id' in session:
            app.logger.info("not login path %s" % path)
            return jsonify(Result().fail(code="user.not.login", msg="user not login"))


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


def page_not_found(error):
    return 'This page does not exist', 404


app.error_handler_spec[None][404] = page_not_found

# app.run(debug=True)
