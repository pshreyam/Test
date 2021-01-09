from flask import Blueprint

student = Blueprint('student', __name__)

@student.route('/')
def index():
    return "Hello, Student!"

@student.route('/app')
def applet():
    return "Hello, Student App!"