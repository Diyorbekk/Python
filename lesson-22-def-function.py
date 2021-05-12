# def - Python-da funktsiya def so'zi yordamida aniqlanadi:
# Python hujjatlarida argumentlar ko'pincha qisqartiriladi va arg.


def hello(name, word):
    print("Hello, " + name + '. Say ' + word)


hello("Diyor", "hi")
hello("Ilhom", "hello")


def get_sum(a, b):
    print(a + b)


x = 2
y = 5

get_sum(1, 3)
get_sum(x, y)


def get_return(a, b):  # return - qaytarib berish
    return a + b


print(get_return(3, 5))


def multiplication_get(a, b):
    print('\nKara jadval\n')

    for i in range(a, b):
        for j in range(a, b):
            print(f'{j} x {i} = {i * j}\t', end='')
        print('')
    else:
        print('\nWell done')


multiplication_get(1, 11)

