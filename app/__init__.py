from flask import Flask

from app.routes import home


def create_app():
    
    app = Flask(__name__)

    home.init(app)

    return app
