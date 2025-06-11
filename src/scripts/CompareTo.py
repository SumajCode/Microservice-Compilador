def compararArreglos(arregloContain: list, arregloComparar: list):
    """
    Compara dos listas de string, verificando si cada string de la segunda 
    lista se encuentra en la primera lista.

    Si alguna de las string de la segunda lista no se encuentra en la primera,
    se devuelve un mensaje con la string que no se encuentra.

    Si todas las string de la segunda lista se encuentran en la primera,
    se devuelve None.

    Parameters
    ----------
    arregloContain : list
        Lista de string que contiene los elementos a comparar
    arregloComparar : list
        Lista de string a comparar con arregloContain

    Returns
    -------
    tuple
        (bool, str) Si se encuentra alguna de las string de arregloComparar
        en arregloContain, se devuelve True y el mensaje de que no se encuentra.
        Si no se encuentra alguna de las string, se devuelve False y None.
    """
    if arregloContain is not None and arregloComparar is not None:
        for string in arregloContain:
            if string in arregloComparar:
                return True, f"No se encuentra en el codigo: {string}"
    return False, None

def compararCodigo(codigos: list, restricciones: list):
    """
    Compara dos listas de string, verificando si la segunda se encuentra
    en la primera.

    Si la segunda lista se encuentra en la primera, se eliminan los
    elementos de la segunda lista de la primera y se devuelve la primera
    lista.

    Si no se encuentra alguna de las restricciones en el codigo, se devuelve
    un mensaje indicando la restriccion que no se encuentra.

    codigos list: El codigo a comparar.
    restricciones list: Las restricciones a comparar.
    :return: Un booleano que indica si no se encuentra alguna de las
             restricciones y un mensaje con la restriccion que no se encuentra.
    """
    if codigos is not None and restricciones is not None:
        tempCodigos = [item.replace(' ', '').replace('\n', '') for item in codigos]
        tempRestricciones = [item.replace(' ', '').replace('\n', '') for item in restricciones]
        i = 0
        for string in tempRestricciones:
            if string not in tempCodigos:
                return True, f"No se encuentra en el codigo: {codigos[i]}"
            i += 1
        i = 0

        for string in codigos:
            if len(codigos) == 1:
                break
            if str(string).lower() in tempRestricciones:
                codigos.remove(string)
    return False, codigos