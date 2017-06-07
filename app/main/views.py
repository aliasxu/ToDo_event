#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import redirect,render_template,flash
from . import main



@main.route('/')
def index():
    return render_template('index.html')