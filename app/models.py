#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from . import db,lm
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True,index=True)
    password = db.Column(db.String(128))
    events = db.relationship('Event',backref='user',lazy='dynamic')

    def check_password(self,password):
        return self.password == password

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except AttributeError:
            raise NotImplementedError('No `id` attribute - override `get_id`')

@lm.user_loader
def load_user(userid):
    return User.query.get(userid)

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(128),unique=True,index=True)
    body = db.Column(db.Text)
    times = db.Column(db.DateTime,default=datetime.utcnow())
    finish = db.Column(db.Boolean,default=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Event %r>' %self.title