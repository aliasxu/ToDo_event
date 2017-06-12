#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import redirect,render_template,flash,url_for
from .. import db
from . import main
from ..models import Event
from forms import TODOForm
from flask_login import login_required,current_user



@main.route('/')
def index():
    if current_user.is_authenticated:
        userid = current_user.id
        event = Event.query.filter_by(user_id=userid)
        return render_template('index.html', events=event)
    return render_template('index.html')

#添加待办事件
@main.route('/add-todo',methods=['GET','POST'])
@login_required
def add_todo():
    form = TODOForm()
    if form.validate_on_submit():
        event = Event(title=form.title.data,
                      body=form.body.data,
                      user=current_user._get_current_object())
        db.session.add(event)
        flash("You event is updated")
        return redirect(url_for('.index'))
    return render_template('todo.html',form=form)

#待办事件详情
@main.route('/detail/<int:id>')
@login_required
def Details(id):
    event = Event.query.get_or_404(id)
    return render_template('detail.html',event=event)
