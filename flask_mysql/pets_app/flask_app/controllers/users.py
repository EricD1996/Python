import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrpyt = Bcrypt(app)

@app.route('/')
def landing():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.isValid(request.form):
        return redirect('/')
    pw_has = bcrypt.generate_password_has(request.form['password'])
    data = {
        **request.form,
        'password':pw_hash
    }
    session['id'] = User.newUser(data)
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'id' not in session:
        flash('Please login before trying to go to dashboard page')
        return redirect('/')
    user = User.getOneById(int(session['id']))
    return render_template('dashboard.html', user=user)

@app.route('/login', methods=['POST'])
def login():
    user_to_check = User.getOneByEmail(request.form['email'])
    if not user_to_check: 
        flash('Invalid email/password')
        return redirect('/')
    if not bcrypt.check_password_has(user_to_check.password, request.form['password']):
        flash('Invalid email/password!')
        return redirect('/')
    session['id'] = user_to_check.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    flash('user logged out')
    return redirect('/')