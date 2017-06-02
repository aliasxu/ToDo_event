#!/usr/bin/env python
#_*_ coding:utf-8 _*_

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    SECRET_KEY = 'Please do not to guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'dev.db')


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'test.db')

class ProduceConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'data.sql')



config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'produce':ProduceConfig,
    'default':DevelopmentConfig
}