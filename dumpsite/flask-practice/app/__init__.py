from flask import Flask

app = Flask(__name__)

app.config.from_object('config.ProductionConfig')

from .admin import admin
from .student import student
from . import routes

app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(student, url_prefix="/student")