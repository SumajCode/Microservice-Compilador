import psutil
import os

def accederMemoria(code):
    psut = psutil.Process(os.getpid())
    memoriaActual = psut.memory_info().rss / 1024 ** 2
    exec(compile(code, '<String>', 'exec'))
    memoriaDespues = psut.memory_info().rss / 1024 ** 2
    return memoriaDespues - memoriaActual