from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "asdfghjkl"

@app.route('/')
def counter():
    return render_template("counter.html")
    
@app.route('/count', methods=['POST'])
def add_counter():
    if not 'number' in session:
        session['number'] = 1
    if 'number' in session:
        session['number'] += 1
    return redirect('/redirect')

@app.route('/redirect')
def redirected():
    return render_template('count.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)


