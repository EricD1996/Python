from flask_app import app
from flask_app.controller import controller_user, controller_routes, controller_movie

if __name__=="__main__":
    app.run(debug=True)
