#Función que recibe como parámetro otra función

def pedir_permiso_a_soleny(respuesta=True):
    print('¿Soleny, Juan José puede salir?')
    print('Mmmmmmmmm')
    if respuesta == False:
        print('si, puede salir')
    else:
        print('No, no puede salir')

def juan_jose_puede_salir(funcion):
    funcion()


print(juan_jose_puede_salir(pedir_permiso_a_soleny))
