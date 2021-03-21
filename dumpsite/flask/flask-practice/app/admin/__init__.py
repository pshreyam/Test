from flask import Blueprint, abort, render_template

admin = Blueprint('admin', __name__, template_folder="admin_templates")

class Color:
    green = "green-1"
    red = "red-2" 
    blue = "blue-3"
    purple = "purple-4"
    orange = "orange-5"

@admin.route('/')
def index():
    return render_template("index.html")

@admin.route('/app')
def applet():
    return "Hello, Admin App!"

@admin.route('colors/<color_id>')
def color(color_id):
    try:
        return getattr(Color(), color_id)
    except AttributeError:
        abort(503)

@admin.errorhandler(503)
def server_error(err):
    return "Error tha re!"