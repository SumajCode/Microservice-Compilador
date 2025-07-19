from flask import Blueprint
from flask import request

from infra.controllers.CodeController import CodeController
from infra.controllers.AssetController import AssetController

compilador = CodeController()
asset = AssetController()
blueprint = Blueprint('code', __name__, url_prefix='/code')

@blueprint.route('/compilar', methods=['POST'])
def compilarCodigo():
    return compilador.compilar(request)

@blueprint.route('/evaluar', methods=['POST'])
def evaluarCodigo():
    return asset.evaluar(request)