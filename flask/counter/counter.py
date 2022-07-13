from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "asdfghjkl"

@app.route('/')
def counter():
    return render_template("counter.html")
    
@app.route('/count', methods=['POST'])
def add_counter():
    session['number'] = 0
    session['number'] += 3
    return redirect('/redirect')

@app.route('/redirect')
def redirected():
    return render_template('count.html')

if __name__=="__main__":
    app.run(debug=True)


