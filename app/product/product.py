from flask import jsonify
from flask_restx import Resource, Namespace
from db.product import get_list


Product = Namespace('Product')

@Product.route('/list', methods=["GET", "POST"])
@Product.doc(params={
        'category': 'An category'
    })
class list(Resource):
    def post(self):
        prod_list = get_list()
        res = {}
        for i in prod_list:
            res[i[0]] = i[1:]
        return jsonify(res)