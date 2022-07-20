from flask_app import app 
from flask import render_template, redirect, session, request
from flask_app.models import model_instrument

#Display Route
@app.route('/instrument/new')
def instrument_new():
    return render_template('instrument_new.html')

# Action Route
@app.route('/instrument/create', methods=['POST'])
def instrument_create():
    # validations
    if not model_instrument.Instrument.validator(request.form):
        return redirect('/instrument/new')
    # create instrument
    data = {
        **request.form,
        'user_id': session['u_id']
    }
    model_instrument.Instrument.create(data)
    return redirect('/')

#Display Route
@app.route('/instrument/<int:id>')
def instrument_show(id):
    return render_template('instrument_show.html')

#Display Route
@app.route('/instrument/<int:id>/edit')
def instrument_edit(id):
    context = {
        'instrument': model_instrument.Instrument.get_one({'id': id})
    }
    return render_template('instrument_edit.html', **context)

#Action Route
@app.route('/instrument/<int:id>/update', methods=['POST'])
def instrument_update(id):
    # validations
    if not model_instrument.Instrument.validator(request.form):
        return redirect(f'/instrument/{id}/edit')
    data = {
        **request.form,
        'id': id
    }
    model_instrument.Instrument.update_one(data)
    return redirect(f'/instrument/{id}/edit')

#Action Route
@app.route('/instrument/<int:id>/delete')
def instrument_delete(id):
    model_instrument.Instrument.delete_one({'id': id})
    return redirect('/')
