"Definimos la tupla"
my_tuple = ()

"Reasignamos la tupla"
my_tuple = (1, 'dos', True)

"Mostramos un valor de la tupla"
print(my_tuple[0])

"creo una nueva tupla y la sumo con la anterior"
my_other_tuple = (2, 3, 4)
my_tuple += my_other_tuple
print(f'La suma de las tuplas es: {my_tuple}')