from flask import request
from flask_restx import Namespace, Resource, fields

from infra.controllers.CodeController import CodeController
from infra.controllers.AssetController import AssetController

ns = Namespace('code', description='Performance code for execution.')
fields_code = ns.model('code', {
    'inputs': fields.List(fields.String),
})

compilador = CodeController()
asset = AssetController()

@ns.route('/compilar')
@ns.doc(params={'code': 'The code to be compiled.', 'lang': 'The language of the code.'})
class CodeCompile(Resource):
    @ns.response(200,'Congratulations.')
    @ns.response(500,'Try again.')
    @ns.doc(responses={200:'Congratulations.', 400:'No wrongs try again.'})
    def post(self):
        """
        Compiles the given code for the given language.

        Parameters
        ----------
        code : str
            The code to be compiled.
        lang : str
            The language of the code.

        Returns
        -------
        Response
            A response of the compilation of the code.
        """
        return compilador.compilar(request)

@ns.route('/evaluar')
@ns.doc(params={
    'code': 'The code to be compiled.',
    'lang': 'The language of the code.',
    'inputs': 'The inputs of the code.',
    'outputs': 'The outputs of the code.',
    'rules': 'The rules of the code.'})
class CodeAsset(Resource):
    @ns.doc(responses={200:'Congratulations.', 400:'No wrongs try again.'})
    @ns.expect(fields_code)
    @ns.marshal_with(fields_code)
    def post(self):
        """
        Evaluate the given code for the given language and inputs.

        Parameters
        ----------
        ``code`` : __str__
            The code to be evaluated.
        lang : str
            The language of the code.
        inputs : list
            The inputs of the code.
        outputs : list
            The outputs of the code.
        rules : list
            The rules of the code.

        Returns
        -------
        Response
            A response of the evaluation of the code.
        """
        return asset.evaluar(request)