from flask import Flask

from app.config import load_config

from app.routes import home, product

from app.extensions import jwt


def create_app():
    
    app = Flask(__name__)
    load_config(app)

    jwt.init(app)

    home.init(app)
    product.init(app)

    return app
