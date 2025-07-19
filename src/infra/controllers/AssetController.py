from features.sandbox.SandBoxCompilerOnlyPython import SandBox
from features.controllers.Controller import Controller
from scripts.FormaterString import formatErrorsValidate
from features.controllers.errors.AssetValidation import AssetForm

class AssetController(Controller):
    def __init__(self):
        super().__init__()
        self.sandbox = SandBox(None)

    def evaluar(self, request):
        """
        Evalúa el código recibido en la solicitud según las entradas y salidas
        proporcionadas.

        El método configura el lenguaje y las entradas/salidas en el objeto
        sandbox y luego llama al método `evaluar` de sandbox para realizar la
        evaluación del código. Si el resultado no contiene errores, devuelve
        una respuesta indicando éxito; de lo contrario, devuelve un mensaje
        de error.

        Parameters
        ----------
        request : Request
            La solicitud HTTP que contiene los datos necesarios para la evaluación,
            incluyendo el código, el lenguaje de programación, las entradas y las
            salidas esperadas.

        Returns
        -------
        Response
            Un objeto de respuesta que contiene el resultado de la evaluación del
            código, un mensaje de éxito o error, el estado y el código de respuesta.
        """
        form = AssetForm(meta={'csrf':False})
        if not form.validate_on_submit():
            return self.response({
                'data':[],
                'message' : formatErrorsValidate(form.errors),
                'status' : 'Error',
                'code':200
            })

        datos =  self.obtenerRequest(request)
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
                'message' : f"Hubo un error con los datos: {e}.",
                'status' : 'Error',
                'code':200
            })