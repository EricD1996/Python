from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import model_movie

@app.route('/movie/new')
def movie():
    if 'u_id' not in session:
        return redirect('/')
    return render_template('movie_new.html')

@app.route('/movie/create', methods=['POST'])
def movie_create():
    if not model_movie.Movie.validator(request.form):
        return redirect('/movie/new')
    data = {
        **request.form,
        'user_id': session['u_id']
    }
    model_movie.Movie.create(data)
    return redirect('/')

@app.route('/movie/<int:id>/view')
def show_movie(id):
    if 'u_id' not in session:
        return redirect('/')
    data = {'id': id}
    movie = model_movie.Movie.get_one_by_id(data)
    return render_template('movie_show.html', movie = movie)

@app.route('/movie/<int:id>/edit')
def movie_edit(id):
    if 'u_id' not in session:
        return redirect('/')
    context = {
        'movie': model_movie.Movie.get_one({'id': id})
    }
    return render_template('movie_edit.html', **context)

@app.route('/movie/<int:id>/update', methods=['POST'])
def movie_update(id):
    if not model_movie.Movie.validator(request.form):
        return redirect(f'/movie/{id}/edit')
    data = {
        **request.form,
        'id': id
    }
    model_movie.Movie.update_one(data)
    return redirect('/')

@app.route('/movie/<int:id>/delete')
def movie_delete(id):
    model_movie.Movie.delete_one({'id': id})
    return redirect('/')