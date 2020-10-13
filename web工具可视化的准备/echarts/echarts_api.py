
from flask import Flask,jsonify,render_template
app = Flask(__name__)


# dt = {"name": '银川市',"data1": [234]}, {"name": '石嘴山市',"data2": [345]}, {"name": '吴忠市',"data3": [453]}, {"name": '固原市',"data4": [320]},{"name": '中卫市',"data5": [213] })

dt = {"d1":[234],"d2":[345],"d3":[453],"d4":[320],"d5":[213]}


# 用js方式取得接口里面json数据的key和value值


@app.route("/")
def index():
    return render_template('bar-tick-align.html')

@app.route('/dataapi', methods=['GET'])
def lsdata():
    return jsonify(dt)



@app.route('/show')
def showDataTable():
    return render_template('from_api.html')

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False # 避免接口汉字出现乱码

    app.run(debug=True)

#  D_T = content.data;
# {
#   "data": [
#     1.5,
#     1.5,
#     1.5,
#     1.5,
#     1.5,
#     1.5,
#     1.5,
#     1.5,


#      series: [{
#            name: '可视化测试',
#            data:D_T,
#            //　数据量太大这种方法就失效了！
#        }],