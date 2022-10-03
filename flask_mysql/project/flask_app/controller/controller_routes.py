from pyexpat import model
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import model_movie
@app.route('/')
def index():
    if 'u_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'u_id' not in session:
        return redirect('/')

    context = {
        'all_movies':  model_movie.Movie.get_all()
    }
    return render_template('dashboard.html', **context)