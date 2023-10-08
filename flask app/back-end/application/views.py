from flask import request, jsonify, Response
from .services.data_service import DataService
from .data.data import mapping, interests_readable, levels_weights
from .app import app
from .models import *
import jsonschema

dataService = DataService(product_schema)


@app.route('/product', methods=['POST'])
@app.validate('product', "product")
def add_product():
    prod = request.get_json()
    new_product = dataService.add_product(prod)
    return product_schema.jsonify(new_product)


@app.route('/products', methods=['POST'])
@app.validate('interests', 'interests')
def get_products():
    data = request.get_json()
    recommended = dataService.get_recommended(data, levels_weights, mapping)
    return jsonify(products_schema.dump(recommended))


@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    return product_schema.jsonify(dataService.get(id))


@app.route('/product/<mobile_id>', methods=['PUT'])
@app.validate('product', "product")
def update_product(mobile_id):
    prod = request.get_json()
    return product_schema.jsonify(dataService.update_product(mobile_id, prod))


@app.route('/product/<mobile_id>', methods=['DELETE'])
def delete_product(mobile_id):
    return product_schema.jsonify(dataService.delete(mobile_id))


@app.route('/top10Battery', methods=['GET'])
def top10Battery():
    result = products_schema.dump(dataService.top10_battery())
    return jsonify(result)


@app.route('/top10Camera', methods=['GET'])
def top10Camera():
    result = products_schema.dump(dataService.top10_camera())
    return jsonify(result)


@app.route('/top10Screen', methods=['GET'])
def top10Screen():
    result = products_schema.dump(dataService.top10_ppi())
    return jsonify(result)


@app.route('/top10cpu', methods=['GET'])
def top10cpu():
    result = products_schema.dump(dataService.top10_cpu())
    return jsonify(result)


@app.route('/interests', methods=['GET'])
def get_interests():
    return jsonify(interests_readable)


@app.errorhandler(jsonschema.ValidationError)
def onValidationError(e):
    return jsonify({"error": 'There was a validation error:'+str(e), "status": 400})
