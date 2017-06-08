#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class TODOForm(FlaskForm):
    title = StringField(u'待办办事件',validators=[DataRequired()])
    body = StringField(u'待办事件内容',validators=[DataRequired()])
    submit = SubmitField(u'提交')