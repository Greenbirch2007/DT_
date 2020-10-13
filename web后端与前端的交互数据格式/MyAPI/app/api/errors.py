


from flask import jsonify
from . import api

@api.app_errorhandler(404)
def page_not_found(e):
    return jsonify({'error': '没有找到您想要的资源', 'code': '404', 'data': ''})

@api.app_errorhandler(500)
def internal_server_error(e):
    return jsonify({'error': '服务器内部错误', 'code': '500', 'data': ''})
