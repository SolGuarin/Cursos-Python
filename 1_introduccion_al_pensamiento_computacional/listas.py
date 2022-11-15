"""
-append: Para incluir un elemento
-pop: Para quitar el último elemento
-remove: Para quitar un elemento dentro de un índice
-insert: para insertar un elemento

"""
"Genero mi lista"
my_list = [1, 2, 3]
"Puedo imprimir las posiciones"
print(my_list[1])
"Agrego nuevos valores"
my_list.append(4)
print(my_list)
"podemos modificar valores"
my_list[0] = 'a'
print(my_list)
"podemos eliminar el último elemento"
my_list.pop()
print(my_list)

"Podemos iterar las listas"
for i in my_list:
    print(i)