def ordenamiento_por_insercion(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

    return lista


if __name__ == '__main__':

    lista = [1, 3, 4, 2, 5]
    
    print(f'Lista es: \n{lista}')
    lista_ordenada = ordenamiento_por_insercion(lista)

    print(f'La lista en ordenada es:\n{lista_ordenada}')


