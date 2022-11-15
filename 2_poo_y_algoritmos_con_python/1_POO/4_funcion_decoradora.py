def funcion_decoradora(funcion):
    def wrapper():
        print('Ultimo mensaje')
        funcion()
        print('primer mensaje')
    return wrapper()

def zumbido():
    print('Buzzzzzz')

zumbido = funcion_decoradora(zumbido)

print(zumbido())
