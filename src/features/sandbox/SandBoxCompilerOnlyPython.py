import subprocess
from domain.errors.WarningsCode import *
from features.compilador.TimeExecute import tiempoEjecucion
from features.compilador.MemoryAccess import accederMemoria
from features.compilador.GetOutputCode import salidaCodigo
from features.compilador.AssertCode import AssertCode
from features.compilador.TaskCode import identificarCodigoEnCodigo
# from compilador.DebbuggerCode import 
# from compilador.MemoryStructure import 

class SandBox(AssertCode):
    def __init__(self, lenguaje: str):
        self.lenguaje = lenguaje
        super().__init__()

    @salidaCodigo()
    @tiempoEjecucion()
    @accederMemoria()
    def compilar(self, datos):
        """
        Compila el codigo segun el lenguaje y la entrada de datos.

        Si el lenguaje es python, se utiliza el compilador de python,
        si no es asi, se utiliza el compilador del lenguaje especificado.

        :param datos: Diccionario que contiene el codigo a compilar,
                      el lenguaje y las entradas y salidas.

        :return: El objeto de compilacion.
        """
        if 'lang' in datos.keys() and 'code' in datos.keys():
            self.code = datos['code']
            if self.lenguaje == 'python':
                super().Compilar()
            elif isinstance(datos['code'], __file__):
                subprocess.Popen([])
        return self

    def evaluar(self, datos: dict):
        """
        Evalua una funcion unica en el codigo.

        El metodo evalua una funcion en el codigo segun las entradas y salidas
        definidas en el diccionario de datos. Si el lenguaje es python, se utiliza
        el compilador de python, si no es asi, se utiliza el compilador del lenguaje
        especificado.

        :param datos: Diccionario que contiene el codigo a evaluar, el lenguaje
                      y las entradas y salidas.

        :return: El objeto de compilacion con los resultados de la evaluacion.
        """
        if 'lang' in datos.keys() and 'code' in datos.keys():
            results = []
            self.entradas = datos['inputs']
            self.salidas = datos['outputs']
            self.functionInvoke = datos['functionInvoke']

            self.todoDelCodigio = identificarCodigoEnCodigo(datos['code'], datos['rules'])
            if isinstance(self.todoDelCodigio, tuple):
                self.salida['result'] = f"{self.todoDelCodigio[0]}:\n{self.todoDelCodigio[1]}"
                return None
            
            if self.lenguaje == 'python':
                if len(self.entradas) == len(self.salidas):
                    for i in range(len(self.entradas)):
                        self.input = self.entradas[i]
                        self.output = self.salidas[i]
                        super().Evaluar(datos['code'])
                        results.append(self.salida)
                        self.salida = {
                            'result':None,
                            'tiempoEjecucion':None,
                            'memoriaUso': None
                        }
                    self.salida = results
                    return self.salida
            elif isinstance(datos['code'], __file__):
                subprocess.Popen([])
        return self