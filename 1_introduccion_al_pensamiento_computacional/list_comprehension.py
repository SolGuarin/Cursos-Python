"Genero una lista del 1 al 100"
my_list = list(range(100))
print(my_list)

"Para doblar los valores de la lista"
double = [i*2 for i in my_list]
print(double)

"Para saber cuales son los pares"
pares = [i for i in my_list if i % 2 == 0]
print(pares)
