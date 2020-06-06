import sys
sys.path.insert(0,'../app/js')
from flask import Flask, render_template,request

#app
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def printcommando():
    return render_template('index.html')

@app.route('/succes', methods=['GET','POST'])
def succes():
    return render_template('succes.html')

#connection with server


if __name__  == "__main__":
	app.run(host='127.0.0.2',port="8000", debug=True)