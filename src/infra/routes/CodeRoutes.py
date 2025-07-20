from flask import Blueprint, request
from flask_restx import Namespace, Resource, fields

from infra.controllers.CodeController import CodeController
from infra.controllers.AssetController import AssetController

ns = Namespace('code', description='Performance code for execution.')

compilador = CodeController()
asset = AssetController()

@ns.route('/compilar', methods=['POST'])
class CodeCompile(Resource):
    @ns.response(200, 'Success')
    def compilarCodigo(self):
        """
        Compila el c digo seg n el lenguaje y la entrada de datos.

        Recibe una solicitud HTTP con los datos necesarios para la compilaci n,
        incluyendo el c digo, el lenguaje de programaci n y las entradas y salidas
        esperadas. El m todo configura el lenguaje y las entradas/salidas en el
        objeto compilador y luego llama al m todo `compilar` de compilador para
        realizar la compilaci n del c digo. Si el resultado no contiene errores,
        devuelve una respuesta indicando xito; de lo contrario, devuelve un
        mensaje de error.

        Returns
        -------
        Response
            Un objeto de respuesta que contiene el resultado de la compilaci n
            del c digo, un mensaje de xito o error, el estado y el c digo de
            respuesta.
        """
        return compilador.compilar(request)

@ns.route('/evaluar', methods=['POST'])
class CodeAsset(Resource):
    def evaluarCodigo(self):
        """
        Evalua el c digo seg n las entradas y salidas proporcionadas.

        Recibe una solicitud HTTP con los datos necesarios para la evaluaci n,
        incluyendo el c digo, el lenguaje de programaci n y las entradas y salidas
        esperadas. El m todo configura el lenguaje y las entradas/salidas en el
        objeto sandbox y luego llama al m todo `evaluar` de sandbox para
        realizar la evaluaci n del c digo. Si el resultado no contiene errores,
        devuelve una respuesta indicando xito; de lo contrario, devuelve un
        mensaje de error.

        Parameters
        ----------
        request : Request
            La solicitud HTTP que contiene los datos necesarios para la evaluaci n,
            incluyendo el c digo, el lenguaje de programaci n y las entradas y salidas
            esperadas.

        Returns
        -------
        Response
            Un objeto de respuesta que contiene el resultado de la evaluaci n del
            c digo, un mensaje de xito o error, el estado y el c digo de respuesta.
        """
        return asset.evaluar(request)