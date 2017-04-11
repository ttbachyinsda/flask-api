from flask import render_template, flash, redirect, session, url_for, request, g  
from flask.ext.login import login_user, logout_user, current_user, login_required  
from app import app, db, lm, models  
from forms import LoginForm  
from models import User  
 
@lm.user_loader  
def load_user(id):  
    return User.query.get(int(id))  
 
@app.before_request  
def before_request():  
    g.user = current_user  
 
@app.route('/')  
@app.route('/index')  
@login_required  
def index ():  
    user=g.user  
    posts=[  
            {'author':{'nickname':'John'},  
             'body':'Beautiful day in Portland!'},  
            {'author':{'nickname':'Susan'},  
             'body':'The Avengers movie was so cool!'}  
           ]  
    return render_template("index.html",  
    title="Home",  
    user=user,  
    posts=posts)  
 
@app.route('/login', methods = ['GET', 'POST'])  
def login():  
    if g.user is not None and g.user.is_authenticated:  
        return redirect(url_for('index'))  
    form = LoginForm()  
    if form.validate_on_submit():  
        if models.User.query.filter_by(nickname=form.openid.data).first():  
            user = User.query.filter_by(nickname=form.openid.data).first_or_404()  
            login_user(user)  
            return redirect(url_for('index'))  
        else:  
            return render_template('login.html',  
        title = 'Sign In',  
        error='[NO]',  
        form = form)  
    return render_template('login.html',  
        title = 'Sign In',  
        form = form)  
 
@app.route('/logout')  
@login_required  
def logout():  
    logout_user()  
    return redirect(url_for('index'))  