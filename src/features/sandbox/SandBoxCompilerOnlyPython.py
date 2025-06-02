import subprocess
from domain.errors.WarningsCode import *
from features.compilador.TimeExecute import tiempoEjecucion
from features.compilador.MemoryAccess import accederMemoria
from features.compilador.GetOutputCode import salidaCodigo
from domain.code.CompilerCode import Compilador
# from compilador.DebbuggerCode import 
# from compilador.MemoryStructure import 

class SandBox(Compilador):
    def __init__(self, lenguaje: str):
        self.lenguaje = lenguaje
        super().__init__()

    @salidaCodigo()
    @tiempoEjecucion()
    @accederMemoria()
    def compilar(self, datos):
        if 'lang' in datos.keys() and 'code' in datos.keys():
            self.code = datos['code']
            if self.lenguaje == 'python':
                super().Compilar()
            elif isinstance(datos['code'], __file__):
                subprocess.Popen([])
        return self
    
    def evaluar(self):
        pass

    def debugg(self):
        pass

    def estrucMemoria(self):
        pass