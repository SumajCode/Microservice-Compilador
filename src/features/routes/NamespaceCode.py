from flask_restx import Namespace, Resource, fields

class NamespaceCode(Namespace):
    def __init__(self, name, description=None, path=None):
        super().__init__(name, description, path)
        self.resource = Resource
        self.fieldsCode = {
            'code': fields.String(),
            'lang': fields.String(),
        }
        self.fieldsCompiler = self.model('code', self.fieldsCode)

        self.fieldsCode['inputs'] = fields.List(fields.String)
        self.fieldsCode['outputs'] = fields.List(fields.String)
        self.fieldsCode['invokFunction'] = fields.String()
        self.fieldsAsset = self.model('asset', self.fieldsCode)
