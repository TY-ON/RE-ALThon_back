from flask import Flask, render_template, redirect, request, session, make_response
from flask_restx import Resource, Api, Namespace
from db.db import insert_user, search_user, delete_user

Product = Namespace('Product')

@Product.route('/list', methods=["GET", "POST"])
@Product.doc(params={
        'category': 'An category'
    })
class register(Resource):
    def post(self):
        return {}