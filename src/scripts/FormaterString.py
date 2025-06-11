def agregarCodigo(code: str, param):

    nuevoCodigo += f"\nprint({str(param) if param  else ''})"

    return code

def eliminarEspaciosLower(arreglo: list):
    return [item.replace(' ', '').lower() for item in arreglo]