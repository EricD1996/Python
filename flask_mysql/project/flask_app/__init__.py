from flask import Flask
app = Flask(__name__)
app.secret_key = "4f7123f5-cc71-4d24-827e-b9030b650e72"
DATABASE = 'movies'

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)