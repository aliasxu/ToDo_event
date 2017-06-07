#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,current_user
from .. import db

from . import auth
from app.models import User
from .forms import RegisterForm,LoginForm

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.name.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Invalid username and password')
    return render_template('auth/login.html',form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logout')
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(name=form.name.data,password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash('Resister success!!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form)





