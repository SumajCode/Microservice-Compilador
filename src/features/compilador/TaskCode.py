from scripts.IdentifyCode import encontrarImports, encontrarFunciones, encontrarClases
from scripts.CompareTo import compararArreglos, compararCodigo

def identificarCodigoEnCodigo(code: str, restricciones: dict):
    """
    Identifica las importaciones, funciones y clases en el codigo y compara
    con las restricciones para ver si cumple con las mismas.

    Parameters
    ----------
    code : str
        El codigo a analizar.

    restricciones : dict
        Las restricciones a comparar.
            - 'imports': lista de importaciones no permitidas.
            - 'functions': dict con las funciones no permitidas.
                - 'functionNames': lista de nombres de funciones no permitidas.
                - 'functionsCode': lista de codigo de las funciones no permitidas.
            - 'classes': dict con las clases no permitidas.
                - 'classNames': lista de nombres de clases no permitidas.
                - 'classesCode': lista de codigo de las clases no permitidas.

    Returns
    -------
    dict
        Un diccionario con los mensajes de error.
            - 'clases': str
                El mensaje de error de las clases.
            - 'funciones': str
                El mensaje de error de las funciones.
    """
    code = code.lower()
    funcionesCodigo = encontrarFunciones(code)
    # clasesCodigo = encontrarClases(code)

    importaciones = None
    # clases = None
    funciones = None

    # restriccionesClases = None
    restriccionesFunciones = None

    keys = restricciones.keys()

    if 'imports' in keys and restricciones['imports']:
        importaciones = [str(importacion).lower().strip() for importacion in restricciones['imports']]
    if 'functions' in keys:
        functionsRules = restricciones['functions']
        keysFuncitons = functionsRules.keys()
        if 'functionNames' in keysFuncitons and functionsRules['functionNames'] is not None:
            funciones = [str(funcion).lower().strip() for funcion in restricciones['functions']['functionNames']]
        if 'functionCodes' in keysFuncitons and functionsRules['functionCodes'] is not None:
            restriccionesFunciones = [str(name).lower().strip() for name in restricciones['functions']['functionsCode']]
    # if 'classes' in keys and restricciones['classes']['classNames'] and restricciones['classes']['classesCode']:
    #     clases = [str(clase).lower().strip() for clase in restricciones['classes']['classNames']]
    #     restriccionesClases = [str(name).lower().strip() for name in restricciones['classes']['classesCode']]
    
    importacionesCodigo = [importacion for importacion in encontrarImports(code)]
    nombreFuncionesCodigo = funcionesCodigo['functionNames']
    # nombreClasesCodigo = clasesCodigo['classNames']

    compararImportaciones, importacion = compararArreglos(
        importacionesCodigo if len(importacionesCodigo) > 0 else None,
        importaciones
    )
    
    # compararClases, mensajeClases = compararCodigo(
    #     nombreClasesCodigo if len(nombreClasesCodigo) > 0 else None,
    #     clases
    # )
    
    compararFunciones, mensajeFunciones = compararCodigo(
        nombreFuncionesCodigo if len(nombreFuncionesCodigo) > 0 else None,
        funciones
    )

    # cambioDeCodigoClases, clasesDeCodigo = compararCodigo(
    #     clasesCodigo['classes'],
    #     restriccionesClases
    # )
    
    cambioDeCodigoFunciones, funcionesDeCodigo = compararCodigo(
        funcionesCodigo['functions'],
        restriccionesFunciones
    )
    
    if compararImportaciones:
        return "Error tiene importaciones no permitidas.", importacion
    if compararFunciones is False:
        # if cambioDeCodigoClases:
        #     return "Error cambio la clase obligatoria.", clasesDeCodigo
        if cambioDeCodigoFunciones:
            return "Error cambio la funcion obligatoria.", funcionesDeCodigo
        return {
            # 'clases': mensajeClases,
            'funciones': mensajeFunciones
        }
    return None