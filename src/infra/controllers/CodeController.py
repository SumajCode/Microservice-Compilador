from domain.errors.ErrorsServer import *
from features.sandbox.SandBoxCompilerOnlyPython import SandBox
from features.controllers.Controller import Controller

class CodeController(Controller):
    def __init__(self):
        super().__init__()
        self.sandobox = SandBox(None)

    def compilar(self, request):
        datos = self.obtenerRequest(request)
        self.sandobox.lenguaje = datos['lang']
        self.sandobox.compilar(datos)
        if 'error' not in str(self.sandobox.salida['result']).lower():
            return self.response({
                'data': self.sandobox.salida,
                'message' : 'A no mame si sabe programar xd.',
                'status' : 'OK',
                'code':200
            })
        return self.response({
            'data': self.sandobox.salida,
            'message' : 'Error al compilar creo que no sirves para programar :v.',
            'status' : 'Error',
            'code':200
        })

    def evaluar(self, codigo: str, lenguaje: str):

        pass

    # def put():
    #     pass