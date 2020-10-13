
from flask import Flask,jsonify,render_template,request
import json
import requests



app = Flask(__name__)

dt = {"data":[{"A":"Hello!","B":"How is it going?","C":3,"D":4},{"A":"These are sample texts","B":0,"C":5,"D":6},{"A":"Mmmm","B":"I do not know what to say","C":7,"D":16},{"A":"Is it enough?","B":"Okay","C":8,"D":9},{"A":"Just one more","B":"...","C":10,"D":11},{"A":"Thanks!","B":"Goodbye.","C":12,"D":13}]}

@app.route('/tabledata', methods=['GET'])
def lsdata():
    return jsonify(dt)

@app.route('/search',methods=['GET'])
def search_form():
    return '''
        <body bgcolor="DodgerBlue">
        <div style="text-align:center">
        <font></font><br/><font></font><br/><font></font><br/>
        <font face="宋体" size="+5" color="#F0F8FF">摇号结果查询</font><br/>
        <font></font><br/>
        <font></font><br/>
        <form action ='/search' methods='POST'>
            <input type="txt"  rows="2" cols="60" placeholder="请输入姓名或编码...."  
            name='username' style="height:40px;width:500px;">  
            <button type="submit" class="search-submit"
            style="height:38px;width:60px;">查询</button> 
        </form>
        </div>
        '''

#  Requests 允许你使用 params 关键字参数，以一个字符串字典来提供这些参数
# 利用request.form.get()语句便能够获取前端输入内容。
#如果访问的是/search页面的post请求，则调用send_ColumnPost（）方法
# 测试代码中的的username就是要选定的字段名
#
@app.route('/search',methods=['POST'])
def search():
    name = request.form['A']#strip去除前后空格 这里已经被赋值了
    if name:
        return send_ColumnPost(name)
    else:
        return render_template('search.html', tips="请输入正确的姓名或编码")

# "Hello!"
def send_ColumnPost(name):
    url = 'http://139.162.19.43:8888/tabledata'
    # data = {
    #     'A': name, # 这里已经被赋值了,
    #     "B":"",
    #     "C":"",
    #     "D":""
    # }
    data = {"A":"{0}".format(name),"B":"How is it going?","C":3,"D":4},
    #使用requests的get请求，返回json格式
    res = requests.get(url=url,params=data).json() # y
    return res
    # #json.dumps将字典转换为json
    # return "<h3>"+json.dumps(res)+"</h3>"



@app.route('/showDT',methods=['GET','POST'])
def showDataTable():
    return render_template('_static_html.html')

if __name__ == '__main__':
    app.run(debug=True)