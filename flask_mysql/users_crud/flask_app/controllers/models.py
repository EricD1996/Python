from flask import render_template,redirect,request,session,flash
from flask_app import app
from model import User
@app.route('/')
def hello_world():
    users = User.get_all()
    print(User)
    return render_template("/read.html", users = users)


@app.route('/move', methods = ['POST'])
def move():
    return redirect('/createpage')


@app.route('/createpage')
def create_page():
    users = User.get_all()
    return render_template("create.html", users = users)

@app.route('/create', methods = ['POST'])
def create():
    User.create(request.form)
    return redirect('/')

@app.route('/show/<int:show_id>')
def show(show_id):
    user = User.get_user({"id":show_id})
    return render_template("show.html", user=user)

@app.route('/edit/<int:edit_id>')
def edit(edit_id):
    user = User.get_user({"id":edit_id})
    return render_template("edit.html", user=user)

@app.route('/edit', methods = ['POST'])
def pedit():
    user = User.edit(request.form)
    return redirect('/')

@app.route('/delete/<int:delete_id>')
def delete(delete_id):
    deleted = User.delete({"id":delete_id})
    return redirect('/',)