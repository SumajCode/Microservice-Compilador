from features.sandbox.SandBoxCompilerOnlyPython import SandBox
from features.controllers.Controller import Controller
from scripts.FormaterString import formatErrorsValidate
from features.controllers.validations.AssetValidation import AssetForm

class AssetController(Controller):
    def __init__(self):
        super().__init__()
        self.sandbox = SandBox(None)

    def evaluar(self, request):
        """
        Evaluate the given code for the given language and inputs.

        Parameters
        ----------
        request: dict
            A dictionary containing the following keys:
            - 'lang': str
                The language of the code.
            - 'inputs': list
                The inputs of the code.
            - 'outputs': list
                The outputs of the code.

        Returns
        -------
        Response
            A response of the evaluation of the code.
        """
        form = AssetForm(meta={'csrf':False})
        if not form.validate_on_submit():
            return self.response({
                'data':[],
                'message' : formatErrorsValidate(form.errors),
                'status' : 'Error',
                'code':200
            })
        datos = self.obtenerRequest(request)
        try:
            self.sandbox.lenguaje = datos['lang']
            self.sandbox.salidas = datos['outputs']
            self.sandbox.entradas = datos['inputs']
            self.sandbox.evaluar(datos)
            salida = self.sandbox.salida
            self.sandbox = SandBox(datos['lang'])
            return self.response({
                'data': salida,
                'message' : 'Resultados de la evaluacion.',
                'status' : 'OK',
                'code':200
            })
        except ValueError as e:
            return self.response({
                'data': [],
                'message' : f"Hubo un error del servidor: {e}.",
                'status' : 'Error',
                'code':500
            })
