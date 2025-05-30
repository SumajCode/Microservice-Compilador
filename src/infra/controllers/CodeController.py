from domain.errors.ErrorsServer import *
from flask import jsonify
from scripts.Compiler import *

class CodeController():
    def __init__(self):
        self.compilador = Compilador()

    def compilar(self, request):
        resultado = self.compilador.Compilar(request)
        if 'error' not in str(resultado['result']).lower():
            return jsonify({
                'data': resultado,
                'message' : 'Compilado con exito. xd',
                'status' : 'OK',
                'code':200
            })
        return jsonify({
            'data': resultado['result'],
            'message' : 'Error al compilar creo que no sirves para programar :v',
            'status' : 'Error',
            'code':200
        })

    def evaluar(self, codigo: str, lenguaje: str):

        pass

    # def put():
    #     pass