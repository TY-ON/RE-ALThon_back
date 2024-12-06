from flask import Flask
from flask import Flask, render_template, redirect, request, session, make_response
from flask_restx import Resource, Api
from login.login import Login # 기능구현한 파일이 여기에서 import된다
from user.user import User
from product.product import Product
from flask_cors import CORS


from db.db import insert_user, search_user, delete_user

app = Flask(__name__)
CORS(app)

api = Api(
    app,
    version='0.1',
    title="OnU",
    description="OnU API Server!",
    terms_url="/",
    contact="ty0507@korea.ac.kr",
    license="MIT"
)


# 이 파일이 아닌 외부에 있는 파일(to_do.py)에 클래스를 구현하고 여기서 import한 다음 add_resource()를 통해 클래스를 등록
api.add_namespace(Login, '/login') # namespace에서 url 들어갈 부분 머로 들어가는지 확인해야함 => 여기선 /todos

api.add_namespace(User, '/user')

api.add_namespace(Product, '/product')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)