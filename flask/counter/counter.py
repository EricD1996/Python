from flask import Flask, render_template, redirect, session
app = Flask(__name__)

@app.route('/')
def counter():
    num = 1
    return render_template("counter.html", num = num)

@app.route('/count', methods=['get'])
def add_counter():
    return redirect('/redirect')

@app.route('/redirect')
def redirected():
    return render_template('counter.html')

if __name__=="__main__":
    app.run(debug=True)


