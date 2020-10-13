
from flask import Flask, Request, request, render_template
import json
import requests



app = Flask(__name__)
@app.route('/search',methods=['GET'])
def search_form():
    return  '''
        <body bgcolor="DodgerBlue">
        <div style="text-align:center">
        <font></font><br/><font></font><br/><font></font><br/>
        <font face="宋体" size="+5" color="#F0F8FF">摇号结果查询</font><br/>
        <font></font><br/>
        <font></font><br/>
        <form action ='/searchresp' method='post'>
            <input type="txt"  rows="2" cols="60" placeholder="请输入姓名或编码...."  
            name='username' style="height:40px;width:500px;">  
            <button type="submit" class="search-submit"
            style="height:38px;width:60px;">查询</button> 
        </form>
        </div>
        '''

#如果访问的是/search页面的post请求，则调用send_ColumnPost（）方法
# 测试代码中的的username就是要选定的字段名

@app.route('/searchresp',methods=['POST'])
def search():
    name = request.form['A'].strip()#strip去除前后空格
    return name
    # if name:
    #     return send_ColumnPost(name)
    # else:
    #     return render_template('search.html', tips="请输入正确的姓名或编码")

#
def send_ColumnPost(name):
    url = 'http://139.162.19.43:8888/tabledata'
    data = {
        'A': name,
        "B":"How is it going?",
        "C":3,
        "D":4
    }
    #使用requests的get请求，返回json格式
    res = requests.get(url=url,params=data).json()
    return res
    # #json.dumps将字典转换为json
    # return "<h3>"+json.dumps(res)+"</h3>"

if __name__ == '__main__':
    app.run()