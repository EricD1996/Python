import math
from tokenize import Number
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<int:num>')
def play2(num):
    newnum = math.floor(num / 4)
    number = num % 4
    return render_template('play2.html',num = num, newnum = newnum, number = number)

@app.route('/play/<int:num>/<color>')
def play3(num, color):
    newnum = math.floor(num / 4)
    number = num % 4
    return render_template('play3.html',num = num, newnum = newnum, number = number, color = color)
 

if __name__=="__main__":
    app.run(debug=True)