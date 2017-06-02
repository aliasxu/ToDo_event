#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,index=True)
    password = db.Column(db.String(128))
    events = db.relationship('Event',backref='user',lazy='dynamic')

    def check_password(self,password):
        return self.password == password



class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(128),unique=True,index=True)
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))