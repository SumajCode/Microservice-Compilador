from flask import jsonify
class Controller:
    def __init__(self):
        pass

    def obtenerRequest(self, request):
        return request.get_json() if request.is_json else request.form

    def response(self, datos):
        return jsonify({
            'data': datos['data'],
            'message' : datos['message'],
            'status' : datos['status'],
            'code':datos['code']
        })