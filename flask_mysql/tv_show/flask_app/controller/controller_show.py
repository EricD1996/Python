from flask_app import app 
from flask import render_template, redirect, session, request
from flask_app.models import model_show

#Display Route
@app.route('/show/new')
def show_new():
    if 'u_id' not in session:
        return redirect('/')
    return render_template('show_new.html')

# Action Route
@app.route('/show/create', methods=['POST'])
def show_create():
    # validations
    if not model_show.Show.validator(request.form):
        return redirect('/show/new')
    # create show
    data = {
        **request.form,
        'user_id': session['u_id']
    }
    model_show.Show.create(data)
    return redirect('/')


#Display Route
@app.route('/show/<int:id>/view')
def show_show(id):
    if 'u_id' not in session:
        return redirect('/')
    data = {'id':id}
    show = model_show.Show.get_one_by_id(data)
    return render_template('show_show.html', show = show)

#Display Route
@app.route('/show/<int:id>/edit')
def show_edit(id):
    if 'u_id' not in session:
        return redirect('/')
    context = {
        'show': model_show.Show.get_one({'id': id})
    }
    return render_template('show_edit.html', **context)

#Action Route
@app.route('/show/<int:id>/update', methods=['POST'])
def show_update(id):
    # validations
    if not model_show.Show.validator(request.form):
        return redirect(f'/show/{id}/edit')
    data = {
        **request.form,
        'id': id
    }
    model_show.Show.update_one(data)
    return redirect('/')

#Action Route
@app.route('/show/<int:id>/delete')
def show_delete(id):
    model_show.Show.delete_one({'id': id})
    return redirect('/')
