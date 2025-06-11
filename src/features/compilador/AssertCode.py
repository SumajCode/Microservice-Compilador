from domain.code.CompilerCode import Compilador
from features.compilador.TimeExecute import tiempoEjecucion
from features.compilador.MemoryAccess import accederMemoria
from features.compilador.GetOutputCode import salidaCodigo
from features.compilador.TaskCode import identificarCodigoEnCodigo
from scripts.FormaterString import agregarCodigo

class AssertCode(Compilador):
    def __init__(self):
        super().__init__()

    @salidaCodigo()
    @tiempoEjecucion()
    @accederMemoria()
    def Evaluar(self, datos: dict):
        """
        Evalua el codigo segun las entradas y salidas definidas en el diccionario de datos.
        
        El metodo evalua el codigo segun las entradas y salidas definidas en el diccionario de datos.
        Si el lenguaje es python, se utiliza el compilador de python, si no es asi, se utiliza el 
        compilador del lenguaje especificado.
        
        Parameters
        ----------
        datos : dict
            Diccionario que contiene el codigo a evaluar, el lenguaje y las entradas y salidas.
        
        Returns
        -------
        dict
            El objeto de compilacion con los resultados de la evaluacion.
        """
        todoDelCodigio = identificarCodigoEnCodigo(datos['code'], datos['rules'])
        if isinstance(todoDelCodigio, tuple):
            self.salida['result'] = f"{todoDelCodigio[0]}:\n{todoDelCodigio[1]}"
            return self.salida
        nuevoCodigo = agregarCodigo(datos['code'], datos['input'], todoDelCodigio)
        self.code = nuevoCodigo
        self.Compilar()
        if self.salida['result'] != datos['output'] :
            self.salida['result'] = f"Error: {self.salida['result']} != {str(datos['output'])}"
        return self.salida