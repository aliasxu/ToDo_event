#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.validators import DataRequired,EqualTo,Length
from ..models import User

class LoginForm(FlaskForm):
    name = StringField('username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login In')

class RegisterForm(FlaskForm):
    name = StringField('username',validators=[DataRequired(),Length(1,64)])
    password1 = PasswordField('password',validators=[DataRequired(),EqualTo('password2',message="Password must be match")])
    password2 = PasswordField('confrim password',validators=[DataRequired()])
    submit = SubmitField(u'注册')

    def validate_name(self,field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('name already register')