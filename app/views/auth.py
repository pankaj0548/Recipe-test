from flask import Blueprint, render_template, url_for, redirect, request, flash, session
from flask_login import current_user, login_user, logout_user, login_required
from app.views import bcrypt
from datetime import datetime, timedelta
from app.db.models import User
from uuid import uuid4
import secrets
import uuid

bp = Blueprint("auth", __name__)
temp_dir = "auth/"

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        password = request.form.get("password")
        conf_pass = request.form.get("conf_pass")
        name = request.form.get("name", '').lower()
        email = request.form.get("email").lower()
        if not password == conf_pass:
            flash("Password does not matched with Confirm Password!","error")
            return redirect(url_for("auth.signup"))

        response = list(User.query.filter_by(email=email))
        if response:
            flash('Email already exist!','error')
            return redirect(url_for('auth.signup'))

        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(
            id = str(uuid4()),
            email = email,
            name = name,
            password = hashed_password,
        )
        user.save()
        return redirect(url_for('auth.login'))

    return render_template(temp_dir + 'signup.html')

@bp.route('/login', methods=['get', 'post'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('recipe.index'))
    if request.method == 'POST':
        email = request.form.get('email').lower()
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            print(user)
            login_user(user)
            print(login_user(user))
            return redirect(url_for('recipe.index'))
        flash("Invalid email or password", "error")
        return redirect(url_for('auth.login'))
    elif request.method == 'GET':
        return render_template(temp_dir + 'login.html')

@bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for('auth.login'))