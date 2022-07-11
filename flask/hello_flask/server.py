from flask import Flask, render_template  
app = Flask(__name__)    


@app.route('/')         
def hello_world():
    return render_template('index.html')


@app.route('/you')
def eric():
    return 'Hello You!'


@app.route('/name/<name>/<int:age>')
def name(name,age):
    return render_template('people.html',name = name, age = age)


if __name__=="__main__":  
    app.run(debug=True)    

