from scripts.IdentifyCode import importsFound, functionsFound
from scripts.CompareTo import arraysCompareTo, codeCompareTo

def identifyCodeInCode(code: str, rules: dict) -> tuple:
    code = code.lower()
    codeFunctions = functionsFound(code)
    # clasesCodigo = encontrarClases(code)

    imports = None
    # clases = None
    functions = None

    # restriccionesClases = None
    restrictionsFunctions = None

    keys = rules.keys()

    if 'imports' in keys and rules['imports']:
        imports = [str(importation).lower().strip() for importation in rules['imports']]
    if 'functions' in keys:
        functionsRules = rules['functions']
        keysFuncitons = functionsRules.keys()
        if 'functionNames' in keysFuncitons and functionsRules['functionNames'] is not None:
            functions = [str(funcion).lower().strip() for funcion in rules['functions']['functionNames']]
        if 'functionCodes' in keysFuncitons and functionsRules['functionCodes'] is not None:
            restrictionsFunctions = [str(name).lower().strip() for name in rules['functions']['functionsCode']]
    # if 'classes' in keys and rules['classes']['classNames'] and rules['classes']['classesCode']:
    #     clases = [str(clase).lower().strip() for clase in rules['classes']['classNames']]
    #     restriccionesClases = [str(name).lower().strip() for name in rules['classes']['classesCode']]
    
    importsCode = importsFound(code)
    nameFunctionsCode = codeFunctions['functionNames']
    # nombreClasesCodigo = clasesCodigo['classNames']

    importsCompareTo, importation = arraysCompareTo(
        importsCode if len(importsCode) > 0 else None,
        imports
    )
    
    # compararClases, mensajeClases = codeCompareTo(
    #     nombreClasesCodigo if len(nombreClasesCodigo) > 0 else None,
    #     clases
    # )
    
    functionCompareTo, functionsMessage = codeCompareTo(
        nameFunctionsCode if len(nameFunctionsCode) > 0 else None,
        functions
    )

    # cambioDeCodigoClases, clasesDeCodigo = codeCompareTo(
    #     clasesCodigo['classes'],
    #     restriccionesClases
    # )
    
    switchFunctionsCode, functionsCode = codeCompareTo(
        codeFunctions['functions'],
        restrictionsFunctions
    )
    
    if importsCompareTo:
        return "Error have imports not allowed.", importation
    if functionCompareTo is False:
        # if cambioDeCodigoClases:
        #     return "Error cambio la clase obligatoria.", clasesDeCodigo
        if switchFunctionsCode:
            return "Error function mandatory switched.", functionsCode
        return {
            # 'clases': mensajeClases,
            'functions': functionsMessage
        }
    return None

def indentifyFunctionExecute(word: str) -> list:
    pass

def identifyArgsForFunction():
    pass