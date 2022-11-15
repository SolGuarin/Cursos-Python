"para definir un diccionario"

"Diccionario con edades"
my_dict = {
    'David': 35,
    'Erika': 32,
    'Jaime': 50,
}
"acceder a un valor a través de una llave"
print(my_dict['David'])

"reasignar un valor"
my_dict['Jaime'] = 20
print(my_dict)

"asignar una nueva llave al diccionario"
my_dict['Pedro'] = 70
print(my_dict)

"borrar una llave con la palabra del"
del my_dict['Jaime']
print(my_dict)

"para iterar el diccionario a través de sus llaves"
for llave in my_dict.keys():
    print(llave)

"para iterar el diccionario a través de sus valores"
for valor in my_dict.values():
    print(valor)

"para iterar el diccionario a través de la llave y el valor"
for llave, valor in my_dict.items():
    print(llave, valor)

"para saber si una llave esta dentro de mi diccionario"
print('David' in my_dict)
print('Sol' in my_dict)