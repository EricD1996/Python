from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template('checkerboard.html')

@app.route('/<int:num>')
def checkerboard2(num):
    return render_template('checkerboard2.html', num = num)

@app.route('/<int:num>/<int:column>')
def checkerboard3(num, column):
    return render_template('checkerboard3.html', num = num, column = column)

@app.route('/<int:num>/<int:column>/<string:color>/<string:color2>')
def checkerboard4(num, column, color, color2):
    return render_template('checkerboard4.html', num = num, column = column, color = color, color2 = color2)



if __name__=="__main__":
    app.run(debug=True)