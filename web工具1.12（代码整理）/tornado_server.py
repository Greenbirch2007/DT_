#! -*- coding:utf-8 -*-


import sys
from tornado.wsgi import WSGIContainer 
from tornado.httpserver import HTTPServer 
from tornado.ioloop import IOLoop 
from f_api_toWeb import app  # 这里导入的是flask项目的运行模块
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000) # flask默认的端口
IOLoop.instance().start()