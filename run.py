#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from app import create_app,db
from app.models import User,Event
from flask_script import  Manager,Shell
from flask_migrate import Migrate,MigrateCommand

app = create_app('default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app,db=db,User=User,Event=Event)

manager.add_command('shell',Shell(make_context=make_shell_context))



if __name__ == '__main__':
    manager.run()