"""
my_list = [1, 1, 2, 3, 3, 4, 5]
print(type(my_list))

my_set = set(my_list)

print(my_set)
"""

# Eliminar repetidos usando set


def eliminar_duplicados(lista):
    my_set = set(lista)
    return my_set


if __name__ == '__main__':
    lista = [8, 8, 8, 8, 9]
    print(eliminar_duplicados(lista))


# Eliminar repetidos usando ciclo for


def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicates_with_sets(some_list):
    return list(set(some_list))


def run():
    random_list = [1, 2, 2, 2, 3, "Platzi", "Platzi", True, 4.6, False]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()



