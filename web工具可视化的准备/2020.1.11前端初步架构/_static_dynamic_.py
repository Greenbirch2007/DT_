
from flask import Flask,jsonify,render_template
app = Flask(__name__)

dt = {"data":[{"A":"Hello!","B":"How is it going?","C":3,"D":4},{"A":"These are sample texts","B":0,"C":5,"D":6},{"A":"Mmmm","B":"I do not know what to say","C":7,"D":16},{"A":"Is it enough?","B":"Okay","C":8,"D":9},{"A":"Just one more","B":"...","C":10,"D":11},{"A":"Thanks!","B":"Goodbye.","C":12,"D":13}]}

@app.route('/tabledata', methods=['GET'])
def lsdata():
    return jsonify(dt)

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/showDT')
def showDataTable():
    return render_template('function1.html')

if __name__ == '__main__':
    app.run(debug=True)