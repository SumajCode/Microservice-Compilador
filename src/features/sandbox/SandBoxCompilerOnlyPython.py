from features.compilador.TimeExecute import tiempoEjecucion
from features.compilador.MemoryAccess import accederMemoria
from features.compilador.GetOutputCode import salidaCodigo
from features.compilador.AssertCode import AssertCode
from features.compilador.TaskCode import identificarCodigoEnCodigo

class SandBox(AssertCode):
    def __init__(self, lenguaje: str):
        self.lenguaje = lenguaje
        self.code = ''
        self.salida = {}
        self.input = None
        self.todoDelCodigio = None
        self.functionInvoke = None
        super().__init__()

    @salidaCodigo()
    @tiempoEjecucion()
    @accederMemoria()
    def compilar(self, datos):
        if 'lang' in datos.keys() and 'code' in datos.keys():
            self.code = datos['code']
            if self.lenguaje == 'python':
                super().Compilar()
        return self

    def evaluar(self, datos: dict):
        if 'lang' in datos.keys() and 'code' in datos.keys():
            results = []
            entradas = datos['inputs']
            salidas = datos['outputs']
            self.functionInvoke = datos['functionInvoke']

            self.todoDelCodigio = identificarCodigoEnCodigo(datos['code'], datos['rules'])
            if isinstance(self.todoDelCodigio, tuple):
                self.salida['result'] = f"{self.todoDelCodigio[0]}:\n{self.todoDelCodigio[1]}"
                return None

            if self.lenguaje == 'python':
                if len(entradas) == len(salidas):
                    for i in enumerate(len(entradas)):
                        self.input = entradas[i]
                        super().Evaluar(datos['code'], output=salidas[i])
                        results.append(self.salida)
                        self.salida = {
                            'result':None,
                            'tiempoEjecucion':None,
                            'memoriaUso': None
                        }
                    self.salida = results
                    return self.salida
        return self