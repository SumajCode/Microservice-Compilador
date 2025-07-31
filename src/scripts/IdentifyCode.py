import re

def functionsFound(code:str):
    patternNames = r'def\s+([a-zA-Z_][a-zA-Z0-9_ ]*)\s*\('
    functionNames = re.findall(pattern=patternNames, string=code, flags=re.IGNORECASE)
    functions = importsRemove(['def' + item for item in code.split('def')])
    return {'functionNames':functionNames, 'functions':functions}

def classesFound(code):
    patternNames = r'class\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*(\(|:)'
    classNames = re.findall(patternNames, code)
    classNames = [nombre[0] for nombre in classNames]
    classes = importsRemove(['class' + item for item in code.split('class')])
    return {'classNames': classNames, 'classes': classes}

def importsFound(code):
    patternImport = r'import\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*'
    return re.findall(pattern=patternImport, string=code, flags=re.IGNORECASE)

def importsRemove(arreglo: list):
    return [item.strip() for item in arreglo if 'import' not in item]