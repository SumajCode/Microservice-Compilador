def agregarCodigo(code: str, param, opciones: dict):
    parametro = formatoParametro(param)
    nuevoCodigo = ""
    clases = [clase.lower() for clase in opciones['clases']]
    funciones = [funcion.lower() for funcion in opciones['clases']]
    if clases and len(clases) > 0:
        if 'main' in clases:
            nuevoCodigo += f"\nmain = {clases}()\n"
    if funciones and len(funciones) > 0:
        if 'main' in funciones:
            nuevoCodigo += f"\nprint({funciones}({parametro}))\n"
    else:
        return "El codigo no es apto para realizar evaluaciones."
    code += nuevoCodigo
    return code

def eliminarEspaciosLower(arreglo: list):
    return [item.replace(' ', '').lower() for item in arreglo]

def formatoParametro(param):
    if isinstance(param, dict):
        return dict(param)
    if isinstance(param, list):
        return list(param)
    if isinstance(param, int):
        return int(param)
    if isinstance(param, str):
        return str(param)
    return