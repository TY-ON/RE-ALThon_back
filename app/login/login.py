from flask import Flask, render_template, redirect, request, session, make_response
from flask_restx import Resource, Api, Namespace
from db.db import insert_user, search_user, delete_user

Login = Namespace('Login')

def post_reg_info(request):
    id = request.form.get("id", False)
    password = request.form.get("password", False)
    username = request.form.get("username", False)
    return id, password, username

@Login.route('/register', methods=["GET", "POST"])
@Login.doc(params={
    'id': 'An ID', 
    'username':"An username",
    'password':'A password'
    })
class register(Resource):
    def post(self):
        id = request.json.get('id')
        password = request.json.get('password')
        username = request.json.get('username')
        
        if not (id and username and password):
            return render_template('/register/failed.html')
        
        if insert_user(id, password, username):
            return render_template('/register/failed.html')
        
        resp = make_response(redirect("./info"))
        resp.set_cookie('username', username)
        session['user:'+username] = username
        return {username}
    def get(self):
        print(session)
        return render_template('/register/register.html')
    
@Login.route('/login', methods=["GET", "POST"])
@Login.doc(params={
    'id': 'An ID', 
    'password':'A password'
    })
class login(Resource):
    def get(self):
        return render_template('/login/login.html')
    
    def post(self):
        id = request.json.get('id')
        password = request.json.get('password')
        
        if not (id and password):
            return render_template('/login/failed.html')
        username = search_user(id, password)
    
        if username:
            session['user:'+username] = username
            resp = make_response(redirect("./info"))
            resp.set_cookie('username', username)
            return {username}
        
        return False

@Login.route("/logout", methods=["GET"])
class logout(Resource):
    def post():
        resp = make_response(redirect("/"))
        resp.set_cookie('username', '', expires=0)
        username = request.cookies.get('username')
        session.pop('user:'+username)
        return {username}

@Login.route("/info/change", methods=["GET", "POST"]) # 수정 필요
class info_change(Resource):
    def get(self):
        return make_response(render_template("./info/change.html"))
    def post(self):
        id = request.json.get('id')
        password = request.json.get('password')
        username = request.json.get('username')
        name = request.cookies.get('username')
        
        if not (id and name and password):
            return make_response(render_template("./info/change.html"))
        
        if delete_user(id, password):
            if insert_user(id, password, username):        
                resp = make_response(redirect("./../info"))
                resp.set_cookie('username', username)
                return {username}
        return False