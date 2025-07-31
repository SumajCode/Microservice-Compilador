from flask import Flask, jsonify
from flask_cors import CORS
from infra.routes.CodeRoutes import ns
from flask_restx import Api

def createApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.conf.BaseConf')
    api = Api(
        app,
        title=app.config['APP_NAME'],
        version=app.config['APP_VERSION'],
        description='Descripcion',
        doc='/docs')
    
    @ns.route('/')
    class Home(ns.resource):
        def get(self):
            """
            Handles GET requests for the root endpoint.

            Returns a JSON response containing the application name and version, a message indicating success, and an HTTP status code.
            """
            return jsonify({
                'data': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
                'message' : 'OK', 
                'status' : 200
            })

    api.add_namespace(ns)
    return app
