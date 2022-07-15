from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

from model import User

@app.route('/')
def hello_world():
    users = User.get_all()
    print(User)
    return render_template("read.html", users = users)


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

if __name__=="__main__":
    app.run(debug=True)

