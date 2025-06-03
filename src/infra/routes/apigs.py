from flask import Flask, Blueprint, jsonify
from flask_cors import CORS

from infra.routes.CodeRoutes import blueprint as blueCode

def createApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.conf.BaseConf')
    padreBlueprint = Blueprint('apicompilador', __name__, url_prefix='/apicompilador/v1')

    @padreBlueprint.route('/')
    def home():
        return jsonify({
            'data': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
            'message' : 'OK', 
            'status' : 200
        })
    
    padreBlueprint.register_blueprint(blueCode)
    app.register_blueprint(padreBlueprint)
    return app
