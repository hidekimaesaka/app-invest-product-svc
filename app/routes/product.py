from flask import Flask, Blueprint, request, jsonify

from flask_jwt_extended import jwt_required, get_jwt_identity


product = Blueprint('product', __name__)


@product.route('/product/new', methods=['POST'])
@jwt_required()
def new_product():
    payload = request.get_json()
    user_id = get_jwt_identity()
    return jsonify(user=user_id)


@product.route('/product/get', methods=['POST'])
@jwt_required()
def get_product():
    payload = request.get_json()
    ...


@product.route('/product/update', methods=['POST'])
@jwt_required()
def update_product():
    payload = request.get_json()
    ...


@product.route('/product/delete', methods=['POST'])
@jwt_required()
def delete_product():
    payload = request.get_json()
    ...


def init(app: Flask):
    app.register_blueprint(product)
