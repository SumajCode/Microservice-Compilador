from flask_restx import Namespace, Resource, fields

class NamespaceCode(Namespace):
    def __init__(self, name, description=None, path=None):
        super().__init__(name, description, path)
        self.resource = Resource
        self.fieldsCode = None
    
    def fieldsCompiler(self):
        self.fieldsCode = {
            'code': fields.String(),
            'lang': fields.String(),
        }
        return self.model('code', self.fieldsCode)

    def fieldsAssert(self):
        self.fieldsCompiler()
        self.fieldsCode['inputs'] = fields.List(fields.String)
        self.fieldsCode['outputs'] = fields.List(fields.String)
        self.fieldsCode['invokFunction'] = fields.String()

        modelFunctions = self.model('functions', {
                'functionNames': fields.List(fields.String),
                'functionCode': fields.List(fields.String)
            })
        modelClass = self.model('class', {
            'classNames': fields.List(fields.String),
            'classCode': fields.List(fields.String)
            })

        self.fieldsCode['rules'] = fields.Nested(self.model('rules', {
            'functions': fields.Nested(modelFunctions),
            'classes': fields.Nested(modelClass)
        }))
        return self.model('asset', self.fieldsCode)