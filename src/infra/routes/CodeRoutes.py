from flask import request

from infra.controllers.CodeController import CodeController
from infra.controllers.AssetController import AssetController
from features.routes.NamespaceCode import NamespaceCode

ns = NamespaceCode(name='code', description='Performance code for execution.', path='/code')

compilador = CodeController()
asset = AssetController()

@ns.route('/compilar')
# @ns.doc(params={'code': 'The code to be compiled.', 'lang': 'The language of the code.'})
class CodeCompile(ns.resource):
    @ns.doc(responses={200: 'Congratulations.', 500: 'No wrongs try again.'})
    @ns.expect(ns.fieldsCompiler())
    def post(self):
        """
        Compiles the given code for the given language.

        Parameters
        ----------
        `code` : *__str__*
            The code to be evaluated.
        `lang` : *__str__*
            The language of the code.

        Returns
        -------
        Response
            A response of the compilation of the code.
        """
        return compilador.compilar(request)

@ns.route('/evaluar')
class CodeAsset(ns.resource):
    @ns.doc(responses={200:'Congratulations.', 400:'No wrongs try again.'})
    @ns.expect(ns.fieldsAssert())
    # @ns.marshal_with(ns.fieldsAsset)
    def post(self):
        """
        Evaluate the given code for the given language and inputs.

        Parameters
        ----------
        `code` : *__str__*
            The code to be evaluated.
        `lang` : str
            The language of the code.
        `inputs` : list
            The inputs of the code.
        `outputs` : list
            The outputs of the code.
        `rules` : list
            The rules of the code.

        Returns
        -------
        Response
            A response of the evaluation of the code.
        """
        return asset.evaluar(request)
