from features.compilador.TaskCode import identificarCodigoEnCodigo

print(identificarCodigoEnCodigo("""def suma(a:int, b: int=3):
    return a+b
""", {
    'imports': None,
    'functions':{
        'functionNames':None,
        'functionsCode':None
    },
    'classes':{
        'classNames':None,
        'classesCode':None
    }
}))