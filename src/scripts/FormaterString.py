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

def formatErrorsValidate(mainErrors):
    """
    Formats validation errors into a single string.

    This function takes a dictionary of validation errors, where each key
    is a field name and each value is a list of error messages. It compiles 
    these errors into a single string where each error is represented as 
    "field:error" and errors are separated by commas.

    Parameters
    ----------
    mainErrors : dict
        A dictionary containing field names as keys and lists of error 
        messages as values.

    Returns
    -------
    str
        A string representation of all errors formatted as "field:error", 
        separated by commas.
    """
    outputErrors = []
    for field, errors in mainErrors.items():
        for error in errors:
            outputErrors.append(f"{field}:{error}")
    return ';\n'.join(outputErrors)