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
        if self.code is not None:
            exec(compile(self.code, '<String>', 'exec'), self.contextGlobal)