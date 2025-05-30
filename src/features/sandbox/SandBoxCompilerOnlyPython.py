import subprocess
from domain.errors.WarningsCode import *
from features.compilador.TimeExecute import tiempoEjecucion
from features.compilador.MemoryAccess import accederMemoria
# from compilador.DebbuggerCode import 
# from compilador.MemoryStructure import 

class SandBox():
    def __init__(self, lenguaje: str):
        self.lenguaje = lenguaje

    def compilar(self, codigo):
        if self.lenguaje == 'python':
            exec(compile(codigo, '<String>', 'exec'))
        elif isinstance(codigo, __file__):
            subprocess.Popen([])
        pass

    def evaluar(self):
        pass

    def debugg(self):
        pass

    def estrucMemoria(self):
        pass