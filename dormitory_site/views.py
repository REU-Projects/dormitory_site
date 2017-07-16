from flask import render_template, flash, redirect
from dormitory_site.server import app
from dormitory_site.forms.login_form import LoginForm
from dormitory_site.models.users import User


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(fullname=form.openid.data).first_or_404()
        return render_template('show_user.html', user=user)
    return render_template('login.html', 
        title = 'Dormitory site',
        form = form)