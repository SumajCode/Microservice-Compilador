from domain.code.CompilerCode import Compilador
from features.compilador.TimeExecute import tiempoEjecucion
from features.compilador.MemoryAccess import accederMemoria
from features.compilador.AssertOutputCode import evaluarSalidaCodigo
from scripts.FormaterString import agregarCodigo

class AssertCode(Compilador):
    def __init__(self):
        self.todoDelCodigio = None
        self.functionInvoke = ""
        self.code = ""
        self.input = None
        self.output = None
        super().__init__()

    @evaluarSalidaCodigo()
    @tiempoEjecucion()
    @accederMemoria()
    def Evaluar(self, codigo: str, **kwargs):
        """
        Evaluates and compiles the given code with specified input and output.

        This method evaluates the provided code by augmenting it with additional
        code structures and inputs, then compiles it while measuring execution time
        and memory usage. It also compares the actual output with the expected output.

        Parameters
        ----------
        codigo : str
            The code to be evaluated and compiled.
        **kwargs : dict
            Additional keyword arguments, including:
            - 'output': The expected output to compare with the actual result.

        Returns
        -------
        self
            The instance with updated compilation results.
        """
        if self.todoDelCodigio:
            self.code = agregarCodigo(codigo, self.input, self.todoDelCodigio, self.functionInvoke)
            self.output = kwargs.get('output')
            self.Compilar(output=self.output)
            return self
