from flask import Flask, jsonify
from flask_cors import CORS
from infra.routes.CodeRoutes import api as blueCode
from flask_restx import Api

def createApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.conf.BaseConf')
    @app.route('/')
    def home():
        return jsonify({
            'data': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
            'message' : 'OK', 
            'status' : 200
        })

    api = Api(
        app,
        title=app.config['APP_NAME'],
        version=app.config['APP_VERSION'],
        description='Descripcion',
        doc='/docs')
    api.add_namespace(blueCode)
    return app
