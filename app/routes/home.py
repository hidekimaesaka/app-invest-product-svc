from flask import Blueprint, Flask

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def home_page():

    return '<h1>Product</h1>'


def init(app: Flask):

    app.register_blueprint(home)
