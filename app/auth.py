from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User, db
from app.forms import LoginForm
from app.decorators import admin_required  # Ensure you have an admin-only decorator

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print("Login Form Loaded\n")
    print(f"Request method: {request.method}")
    print(f"Form data: {request.form}")  # Print raw form data

    if request.method == 'POST':
        print("POST request detected!")
        print(f"CSRF Token in Form: {form.csrf_token.data}")  # Debug CSRF Token

        ret = form.validate_on_submit()
        print("Ret = ", ret)
        print("Form errors:", form.errors)  # Debugging form validation errors

        if ret:
            user = User.query.filter_by(email=form.email.data).first()
            print("Hashed:")
            print(generate_password_hash("password"))
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                print("Password Check Successful\n")
                flash('Login successful', 'success')
                return redirect(url_for('routes.seat_selection'))  # Redirect to seat selection page
            else:
                print("Password Check Unsuccessful\n")
                flash('Invalid email or password', 'danger')
        else:
            flash('Form validation failed', 'danger')
    print("Login Form Completed\n")
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
@admin_required  # Only admins can create new users
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        is_admin = bool(request.form.get('is_admin'))  # Checkbox for admin creation

        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'danger')
            return redirect(url_for('auth.register'))

        hashed_password = generate_password_hash(password)
        new_user = User(email=email, password=hashed_password, is_admin=is_admin)
        db.session.add(new_user)
        db.session.commit()

        flash('User registered successfully', 'success')
        return redirect(url_for('routes.dashboard'))  # Change to an appropriate route

    return render_template('register.html')
