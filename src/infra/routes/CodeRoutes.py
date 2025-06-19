from flask import Blueprint
from flask import request

from infra.controllers.CodeController import CodeController

compilador = CodeController()
blueprint = Blueprint('code', __name__, url_prefix='/code')

@blueprint.route('/compilar', methods=['POST'])
def compilarCodigo():
    return compilador.compilar(request)

@blueprint.route('/evaluar', methods=['POST'])
def evaluarCodigo():
    return compilador.evaluar(request)