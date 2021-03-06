#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
lm = LoginManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    lm.init_app(app)

    from app.auth import auth
    app.register_blueprint(auth,url_prefix='/auth')

    from app.main import main
    app.register_blueprint(main)

    return app