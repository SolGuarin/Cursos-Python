
import time


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n-1)


if __name__ == '__main__':
    n = 100000

    print('Factorial normal')
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    print('')

    print('factorial recursivo')
    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)



