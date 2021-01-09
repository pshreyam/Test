from . import app

@app.errorhandler(404)
def error_handler(e):
    return "Sorry! No page found!"