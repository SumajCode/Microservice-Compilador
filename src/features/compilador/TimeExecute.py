import time

def tiempoEjecucion(codigo):
    tiempoIni = time.time()
    exec(compile(codigo, '<String>', 'exec'))
    tiempoFin = time.time()
    return tiempoFin - tiempoIni