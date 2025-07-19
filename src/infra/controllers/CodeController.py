from features.sandbox.SandBoxCompilerOnlyPython import SandBox
from features.controllers.errors.CompilerValidation import CodeForm
from features.controllers.Controller import Controller
from scripts.FormaterString import formatErrorsValidate

class CodeController(Controller):

    def __init__(self):
        super().__init__()
        self.sandbox = SandBox(None)

    def compilar(self, request):
        """
        Compila el código segun el lenguaje y la entrada de datos.

        Recibe una solicitud HTTP con los datos necesarios para la compilación,
        incluyendo el código, el lenguaje de programación y las entradas y salidas
        esperadas. El método configura el lenguaje y las entradas/salidas en el
        objeto sandbox y luego llama al método `compilar` de sandbox para
        realizar la compilación del código. Si el resultado no contiene errores,
        devuelve una respuesta indicando éxito; de lo contrario, devuelve un
        mensaje de error.

        Parameters
        ----------
        request : Request
            La solicitud HTTP que contiene los datos necesarios para la
            compilación, incluyendo el código, el lenguaje de programación y las
            entradas y salidas esperadas.

        Returns
        -------
        Response
            Un objeto de respuesta que contiene el resultado de la compilación
            del código, un mensaje de éxito o error, el estado y el código de
            respuesta.
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
