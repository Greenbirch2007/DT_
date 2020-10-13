



from flask import Flask,jsonify,render_template
app = Flask(__name__)

dt = {"Rows":[{"truePay":30.0,"shouldPay":140.0,"year":"2013"},{"truePay":140.0,"shouldPay":140.0,"year":"2012"},{"truePay":134.5,"shouldPay":140.0,"year":"2011"},{"truePay":141.0,"shouldPay":140.0,"year":"2010"},{"truePay":85.0,"shouldPay":86.5,"year":"2009"}],"RowCount":5}


@app.route("/")
def index():
    return "<h1>测试Highcharts写接口</h1>"

@app.route('/dataapi', methods=['GET'])
def lsdata():
    return jsonify(dt)



@app.route('/show')
def showDataTable():
    return render_template('index.html')

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False # 避免接口汉字出现乱码

    app.run(debug=True)


