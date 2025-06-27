class Compilador:
    def __init__(self):
        self.code = None
        self.contextGlobal = {}
        self.salida = {
            'result':None,
            'tiempoEjecucion':None,
            'memoriaUso': None
        }
    
    def Compilar(self, **kwargs):
        """
        Compila el codigo en el lenguaje especificado en el atributo lenguaje.

        El metodo compila el codigo en el lenguaje especificado en el atributo lenguaje.
        Si el lenguaje es python, se utiliza el compilador de python, si no es asi, se utiliza el 
        compilador del lenguaje especificado.

        Parameters
        ----------
        **kwargs
            Diccionario que contiene el codigo a compilar y el lenguaje.

        Returns
        -------
        dict
            El objeto de compilacion con los resultados de la compilacion.
        """
        if self.code is not None:
            exec(compile(self.code, '<String>', 'exec'), self.contextGlobal)