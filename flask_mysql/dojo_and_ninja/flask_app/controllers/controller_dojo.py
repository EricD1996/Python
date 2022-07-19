from flask_app import app, bcrypt
from flask import render_template, redirect, session, request
# Display Route
from flask_app.models import model_dojo
from flask_app.models import model_ninja

@app.route('/')
def index():
    dojos = model_dojo.Dojo.get_all()
    print(model_dojo.Dojo)
    return render_template('index.html', dojos = dojos)
    
@app.route('/dojo/new')
def dojo_new():
    return render_template('dojo_new.html')

#Action Route
@app.route('/dojo/create', methods=['POST'])
def dojo_create():
    model_dojo.Dojo.create(request.form)
    return redirect('/')

# display Route
@app.route('/dojo/<int:id>')
def dojo_show(id):
    dojo = model_dojo.Dojo.get_dojo_with_ninja({"id":id})
    return render_template('dojo.html', dojo = dojo)
