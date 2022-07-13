from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "qwertyuiop"

@app.route('/')
def survey():
    return render_template('dojo_survey.html')

@app.route('/process', methods=['POST'])
def process():
    print(f"You have now purchased a new {request.form['name']}")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')   

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=="__main__":
    app.run(debug=True)

