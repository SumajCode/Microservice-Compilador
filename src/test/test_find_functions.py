from scripts.IdentifyCode import encontrarFunciones

print(encontrarFunciones("""
import random
def prueba(maxnumero: int):
    return f\"Prueba de random {random.randint(0, maxnumero)}\"
def prueba(maxnumero: int):
    return f\"Prueba de random {random.randint(0, maxnumero)}\"
def prueba(maxnumero: int):
    return f\"Prueba de random {random.randint(0, maxnumero)}\"
print(prueba(6))
"""))