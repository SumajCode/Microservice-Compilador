from scripts.IdentifyCode import encontrarImports

print(encontrarImports("""
import random
from flask_cors import CORS
def prueba(maxnumero: int):
    return f\"Prueba de random {random.randint(0, maxnumero)}\"
print(prueba(6))
"""))