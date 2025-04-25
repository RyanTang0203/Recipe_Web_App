from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from .models import db, User
from .forms import LoginForm, RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
from app import myapp_obj

@myapp_obj.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Username already taken. Please choose a different one.')
            return render_template('register.html', form=form)

        hashed_pw = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@myapp_obj.route('/home')
@login_required
def home():
	return render_template('home.html')
	
@myapp_obj.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))
