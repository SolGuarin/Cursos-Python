"""Definir un rango
range(comienzo, fin, pasos
"""

my_range = range(1, 5)
print(type(my_range))
"uso un for para mostrar el rango que he generado "
for i in my_range:
    print(i)

"para general la secuencia de números pares hasta el 100"
"le digo que empiece en 0, vaya hasta 101 y que lo haga de 2 en 2"
for i in range(0, 101, 2):
    print(i)
"Secuencia de números impares hasta el 100"
for i in range(1, 100, 2):
    print(i)