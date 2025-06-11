from features.compilador.TaskCode import identificarCodigoEnCodigo

print(identificarCodigoEnCodigo("""
import random
class prueba:
    def prueba(maxnumero: int):
        return f\"Prueba de random {random.randint(0, maxnumero)}\"
    def prueba(maxnumero: int):
        return f\"Prueba de random {random.randint(0, maxnumero)}\"
    def prueba(maxnumero: int):
        return f\"Prueba de random {random.randint(0, maxnumero)}\"
""", {
    'imports': ['random'],
    'functions':{
        'functionNames':None,
        'functionsCode':None
    },
    'classes':{
        'classNames':None,
        'classesCode':None
    }
}))