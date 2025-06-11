import re

def encontrarFunciones(code:str):    
    """
    Identifica las funciones en el código.

    Busca en el código las definiciones de funciones y las devuelve en un 
    diccionario con dos claves: "functionNames" y "functions". La primera, 
    contiene una lista de los nombres de las funciones encontradas, mientras 
    que la segunda contiene las definiciones completas de las funciones.

    Parameters
    ----------
    code : str
        El código a analizar.

    Returns
    -------
    dict
        Un diccionario con las funciones encontradas.
    """

    patternNombres = r'def\s+([a-zA-Z_][a-zA-Z0-9_ ]*)\s*\('
    nombreFunciones = re.findall(pattern=patternNombres, string=code, flags=re.IGNORECASE)
    funciones = eliminarImports(['def' + item for item in code.split('def')])
    return {'functionNames':nombreFunciones, 'functions':funciones}

def encontrarClases(code):
    """
    Identifica las clases en el c digo.

    Busca en el c digo las definiciones de clases y las devuelve en un diccionario
    con dos claves: "classNames" y "classes". La primera, contiene una lista de
    los nombres de las clases encontradas, mientras que la segunda contiene
    las definiciones completas de las clases.

    Parameters
    ----------
    code : str
        El c digo a analizar.

    Returns
    -------
    dict
        Un diccionario con las clases encontradas.
    """
    patternNombres = r'class\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*(\(|:)'
    nombreClases = re.findall(patternNombres, code)
    nombreClases = [nombre[0] for nombre in nombreClases]
    clases = eliminarImports(['class' + item for item in code.split('class')])
    return {'classNames': nombreClases, 'classes': clases}

def encontrarImports(code):
    """
    Busca los imports en el codigo y los devuelve como una lista de nombres.
    
    Parameters
    ----------
    code : str
        El codigo donde se busca los imports.
    
    Returns
    -------
    imports : list
        Una lista de nombres de imports encontrados.
    """
    patternImport = r'import\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*'
    return re.findall(pattern=patternImport, string=code, flags=re.IGNORECASE)

def eliminarImports(arreglo: list):
    return [item.strip() for item in arreglo if 'import' not in item]