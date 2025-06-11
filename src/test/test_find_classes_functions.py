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
    'imports': None,
    'functions':{
        'functionNames':['prueba'],
        'functionsCode':["""
    def prueba(maxnumero: int):
        return f\"Prueba de random {random.randint(0, maxnumero)}\"
"""]
    },
    'classes':{
        'classNames':['prueba'],
        'classesCode':["""
class prueba:
    def prueba(maxnumero: int):
        return f\"Prueba de random {random.randint(0, maxnumero)}\"
    def prueba(maxnumero: int):
        return f\"Prueba de random {random.randint(0, maxnumero)}\"
    def prueba(maxnumero: int):
        return f\"Prueba de random {random.randint(0, maxnumero)}\"
"""]
    }
}))