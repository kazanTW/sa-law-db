from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restful import Api
from .utils.db import db
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    Migrate(app, db)
    CORS(app)  # 啟用跨域處理
    api = Api(app)

    register_routes(api)  # 註冊 API 路由

    return app
