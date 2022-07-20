from flask_app import app 
from flask import render_template, redirect, session, request
from flask_app.models import model_recipe

#Display Route
@app.route('/recipe/new')
def recipe_new():
    return render_template('recipe_new.html')

# Action Route
@app.route('/recipe/create', methods=['POST'])
def recipe_create():
    # validations
    if not model_recipe.Recipe.validator(request.form):
        return redirect('/recipe/new')
    # create recipe
    data = {
        **request.form,
        'user_id': session['u_id']
    }
    model_recipe.Recipe.create(data)
    return redirect('/')


#Display Route
@app.route('/recipe/<int:id>/view')
def recipe_show(id):
    data = {'id':id}
    recipe = model_recipe.Recipe.get_one(data)
    return render_template('recipe_show.html', recipe = recipe)

#Display Route
@app.route('/recipe/<int:id>/edit')
def recipe_edit(id):
    context = {
        'recipe': model_recipe.Recipe.get_one({'id': id})
    }
    return render_template('recipe_edit.html', **context)

#Action Route
@app.route('/recipe/<int:id>/update', methods=['POST'])
def recipe_update(id):
    # validations
    if not model_recipe.Recipe.validator(request.form):
        return redirect(f'/recipe/{id}/edit')
    data = {
        **request.form,
        'id': id
    }
    model_recipe.Recipe.update_one(data)
    return redirect('/')

#Action Route
@app.route('/recipe/<int:id>/delete')
def recipe_delete(id):
    model_recipe.Recipe.delete_one({'id': id})
    return redirect('/')
