from flask_app import app, bcrypt
from flask import render_template, redirect, session, request
from flask_app.models import model_ninja
from flask_app.models import model_dojo

# Display Route
@app.route('/ninja/new')
def ninja_new():
    dojos = model_dojo.Dojo.get_all()
    return render_template('ninja.html', dojos = dojos)

#Action Route
@app.route('/ninja/create', methods=['POST'])
def ninja_create():
    model_ninja.Ninja.create(request.form)
    return redirect('/')

# display Route
@app.route('/ninja/<int:id>')
def ninja_show(id):
    return render_template('ninja_show.html')

# Display Route
@app.route('/ninja/<int:id>/edit')
def ninja_edit(id):
    return render_template('ninja_edit.html')

#Action Route
@app.route('/ninja/<int:id>/update', methods=['POST'])
def ninja_update(id):
    return redirect('/')

#Action Route
@app.route('/ninja/<int:id>/delete')
def ninja_delete(id):
    return redirect('/')
