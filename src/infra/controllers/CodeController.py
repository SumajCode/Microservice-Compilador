from features.sandbox.SandBoxCompilerOnlyPython import SandBox
from features.controllers.validations.CompilerValidation import CodeForm
from features.controllers.Controller import Controller
from scripts.FormaterString import formatErrorsValidate

class CodeController(Controller):

    def __init__(self):
        super().__init__()
        self.sandbox = SandBox(None)

    def compilar(self, request):
        """
        Compiles the given code for the given language.

        Parameters
        ----------
        request: dict
            A dictionary containing the following keys:
            - 'code': str
                The code to be compiled.
            - 'lang': str
                The language of the code.

        Returns
        -------
        Response
            A response of the compilation of the code.
        """
        form = CodeForm(meta={'csrf':False})
        if not form.validate_on_submit():
            return self.response({
                'data':[],
                'message': formatErrorsValidate(form.errors),
                'status': 'Error',
                'code': 200
            })

        try:
            datos = self.obtenerRequest(request)
            self.sandbox.lenguaje = datos['lang']
            self.sandbox.compilar(datos)
            salida = self.sandbox.salida
            self.sandbox = SandBox(datos['lang'])
            if 'error' not in str(self.sandbox.salida['result']).lower():
                return self.response({
                    'data': salida,
                    'message' : 'A no mame si sabe programar xd.',
                    'status' : 'OK',
                    'code':200
                })
            return self.response({
                'data': salida,
                'message' : 'Error al compilar creo que no sirves para programar :v.',
                'status' : 'Error',
                'code':200
            })
        except ValueError as e:
            return self.response({
                'data': [],
                'message' : f"Hubo un error con el servidor: {e}.",
                'status' : 500,
            })
