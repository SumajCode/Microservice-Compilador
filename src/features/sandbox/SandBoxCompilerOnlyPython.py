from features.compilador.TimeExecute import tiempoEjecucion
from features.compilador.MemoryAccess import accederMemoria
from features.compilador.GetOutputCode import salidaCodigo
from features.compilador.AssertCode import AssertCode
from features.compilador.TaskCode import identifyCodeInCode

class SandBox(AssertCode):
    def __init__(self, lenguaje: str):
        self.lenguaje = lenguaje
        self.code = ''
        self.salida = {}
        self.input = None
        self.allAboutCode = None
        self.functionInvoke = None
        super().__init__()

    @salidaCodigo()
    @tiempoEjecucion()
    @accederMemoria()
    def compilar(self, datos: dict) -> dict:
        """
        Compiles the provided code for the specified language.

        This method compiles the code contained in the 'datos' dictionary
        if both 'lang' and 'code' keys are present. The compilation process
        is executed if the language is Python, utilizing the parent class's
        compilation method. During the process, execution time, memory usage,
        and standard output are measured and captured.

        Parameters
        ----------
        datos : dict
            A dictionary that must contain the keys:
            - 'lang': The language of the code.
            - 'code': The source code to be compiled.

        Returns
        -------
        dict
            The instance with updated compilation results.
        """
        if 'lang' in datos.keys() and 'code' in datos.keys():
            self.code = datos['code']
            if self.lenguaje == 'python':
                super().Compilar()
        return self

    def evaluar(self, data: dict) -> dict:
        """
        Evaluate the given code for the given language and inputs.

        Parameters
        ----------
        data: dict
            A dictionary containing the following keys:
            - 'lang': str
                The language of the code.
            - 'code': str
                The code to be evaluated.
            - 'inputs': list
                The inputs of the code.
            - 'outputs': list
                The outputs of the code.
            - 'functionInvoke': str
                The function to invoke in the code.
            - 'rules': list
                The rules of the code.

        Returns
        -------
        dict
            A dictionary containing the results of the evaluation of the code.
        """
        if 'lang' in data.keys() and 'code' in data.keys():
            results = []
            inputs = data['inputs']
            outputs = data['outputs']
            self.functionInvoke = data['functionInvoke']
            self.allAboutCode = identifyCodeInCode(data['code'], data['rules'])

            if isinstance(self.allAboutCode, tuple):
                self.salida['result'] = f"{self.allAboutCode[0]}: {self.allAboutCode[1]}"
                return None

            if self.lenguaje == 'python':
                if len(inputs) == len(outputs):
                    for i in enumerate(len(inputs)):
                        self.input = inputs[i]
                        super().Evaluar(data['code'], output=outputs[i])
                        results.append(self.salida)
                        self.salida = {'result': None, 'time_execution': None, 'memory_used': None}
                    self.salida = results
                    return self.salida
        return self

    def debbuger(self):
        pass