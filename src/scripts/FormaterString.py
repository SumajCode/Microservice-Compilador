def agregarCodigo(code: str, param, opciones: dict, functionInvoke: str):
    parametro = formatoParametro(param)
    nuevoCodigo = code
    # clases = [clase.lower() for clase in opciones['clases']]
    funciones = [funcion.lower() for funcion in opciones['funciones']]
    # if clases and len(clases) > 0:
    #     if 'main' in clases:
    #         clase = opciones['clases'][clases.index('main')]
    #         nuevoCodigo += f"\nmain = {clase}()"
    # else:
    #     return "El codigo no es apto para realizar evaluaciones.\nFalta la clase main."
    if funciones and len(funciones) > 0:
        if functionInvoke in funciones:
            nuevoCodigo += f"\nprint({functionInvoke}({parametro}))\n"
    else:
        return "El codigo no es apto para realizar evaluaciones.\nFalta una funcion main."
    # print("Nuevo codigo: ", code)
    return nuevoCodigo

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
    return None