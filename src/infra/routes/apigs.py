from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from infra.controllers.CodeController import CodeController

def createApp():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object('config.conf.BaseConf')
    return app

app = createApp()

# @app.errorhandler(HTTPException)
# def handle_error(e):
#     return jsonify({
#         'data': e.description, 
#         'message' : e.name, 
#         'status' : e.code
#     }), e.code

@app.route('/')
def home():
    return jsonify({
        'data': f"{app.config['APP_NAME']+ '-' + app.config['APP_VERSION']} is running", 
        'message' : 'OK', 
        'status' : 200
    })

@app.route('/compilarCodigo', methods=['POST'])
def compilarCodigo():    
    return CodeController().compilar(request)

@app.route('/evaluarCodigo')
def compiler():
    return 
# @app.route('/error')
# def handleErrors():
#     if () :
#         raise ServerError()

if __name__ == '__main__' :
    app.run()