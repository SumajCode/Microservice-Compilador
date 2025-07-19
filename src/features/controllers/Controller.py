from flask import jsonify
class Controller:
    def __init__(self):
        pass

    def obtenerRequest(self, request):
        """
        Obtiene los datos del request en formato dict.
        
        request (Request): El request que contiene los datos a obtener.
        
        Return:
            dict: Un diccionario con los datos del request.
        """
        return request.get_json() if request.is_json else request.form

    def response(self, datos):
        """
        Construye una respuesta HTTP con los datos dados.
        
        datos (dict): Diccionario que contiene la informacion para la respuesta.
            Debe tener las claves 'data', 'message', 'status' y 'code'.
        
        Return:
            Response: Un objeto de respuesta HTTP con los datos dados.
        """
        return jsonify({
            'data': datos['data'],
            'message' : datos['message'],
            'status' : datos['status'],
            'code':datos['code']
        })