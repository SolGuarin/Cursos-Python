import time


def fibo_gen(nMax: int):
    n1 = 0
    n2 = 1
    counter = 0
    while counter < nMax:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


if __name__ == '__main__':

    nMax = (int(input("¿Cuántos números quiere imprimir?: ")))
    fibonacci = fibo_gen(nMax)
    for element in fibonacci:
        print(element)
        time.sleep(.05)
