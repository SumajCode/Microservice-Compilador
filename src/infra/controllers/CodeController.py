from domain.errors.ErrorsServer import *
from features.sandbox.SandBoxCompilerOnlyPython import SandBox
from features.controllers.Controller import Controller

class CodeController(Controller):
    def __init__(self):
        super().__init__()
        self.sandbox = SandBox(None)

    def compilar(self, request):
        datos = self.obtenerRequest(request)
        self.sandbox.lenguaje = datos['lang']
        self.sandbox.compilar(datos)
        if 'error' not in str(self.sandbox.salida['result']).lower():
            return self.response({
                'data': self.sandbox.salida,
                'message' : 'A no mame si sabe programar xd.',
                'status' : 'OK',
                'code':200
            })
        return self.response({
            'data': self.sandbox.salida,
            'message' : 'Error al compilar creo que no sirves para programar :v.',
            'status' : 'Error',
            'code':200
        })

    def evaluar(self, request):
        datos =  self.obtenerRequest(request)
        self.sandbox.lenguaje = datos['lang']
        self.sandbox.salidas = datos['outputs']
        self.sandbox.entradas = datos['inputs']
        if datos['lang'] is not None and datos['outputs'] is not None and datos['inputs'] is not None:
            self.sandbox.evaluar(datos)
            if 'error' not in str(self.sandbox.salida['result']).lower():
                return self.response({
                    'data': self.sandbox.salida,
                    'message' : 'A no mame si sabe programar xd.',
                    'status' : 'OK',
                    'code':200
                })
        return self.response({
            'data': self.sandbox.salida,
            'message' : 'Error al compilar creo que no sirves para programar :v.',
            'status' : 'Error',
            'code':200
        })

    # def put():
    #     pas