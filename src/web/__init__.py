from flask import Flask

print("view init file")
app = Flask(__name__)


from web.views import view,area_view
from web.manager import user

app.register_blueprint(view.mod)
app.register_blueprint(user.muser,url_prefix='/manager')
app.register_blueprint(area_view.area,url_prefix='/base')