from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def name(name):
    return f"Hi {name}"

@app.route('/repeat/<word>/<int:num>')
def repeat(word, num):
    return f"{word} \n"*num

if __name__=="__main__":
    app.run(debug=True)