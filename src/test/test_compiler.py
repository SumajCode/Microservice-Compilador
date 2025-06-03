from scripts.Compiler import Compilador


def compilar_test(datos):
    return exec(compile(datos['code'], '<String>', 'exec'))

compilar_test({
    'code':'''
def imprimir():
    print('hola')
imprimir()
    '''
})

# compilador = Compilador()
# compilador.Compilar(request(jsonify({
#     'code':'''
#     def imprimir():
#         print('hola')
#     imprimir()
#     ''',
#     'lang':'python'
# })))