from flask_app import app, bcrypt
from flask import render_template, redirect, session, request
from flask_app.models import model_user

#Display Route
@app.route('/user/login', methods=['post'])
def user_new():
    #validate
    model_user.User.validator_login(request.form)
    return redirect('/')

@app.route('/user/create', methods=['POST'])
def user_create():
    # validations
    if not model_user.User.validator(request.form):
        return redirect('/')

    # hashing
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
    data = {
        **request.form,
        'pw': hash_pw
    }

    # create my user
    id = model_user.User.create(data)

    # store user_id in session
    session['u_id'] = id
    return redirect('/dashboard')

@app.route('/user/logout')
def logout_user():
    del session['u_id']
    return redirect('/')

#Display Route
@app.route('/user/<int:id>')
def user_show(id):
    return render_template('user_show.html')

#Display Route
@app.route('/user/<int:id>/edit')
def user_edit(id):
    return render_template('user_edit.html')

#Action Route
@app.route('/user/<int:id>/update', methods=['POST'])
def user_update(id):
    return redirect('/')

#Action Route
@app.route('/user/<int:id>/delete')
def user_delete(id):
    return redirect('/')