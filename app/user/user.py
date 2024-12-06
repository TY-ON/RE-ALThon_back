from flask import Flask, render_template, redirect, request, session, make_response
from flask_restx import Resource, Api, Namespace
from db.db import insert_user, search_user, delete_user

User = Namespace('User')

def post_reg_info(request):
    id = request.form.get("id", False)
    password = request.form.get("password", False)
    username = request.form.get("username", False)
    return id, password, username

@User.route('/register', methods=["GET", "POST"])
@User.doc(params={
    'id': 'An ID', 
    'username':"An username",
    'password':'A password'
    })
class register(Resource):
    def post(self):
        return {}