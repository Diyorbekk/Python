# def documentation - funksiya haqida dokumitatsiya


def get_sum(a, b):
    """
    a va b argumentlarni yig'indisni qaytaradi.



    :param a: birinchi operand
    :type a: int
    :param b: ikkinchi operand
    :type b: int
    :return: Return type int
    """
    return a + b


print(get_sum(1, 2))

# global and local - global va local.

a = 5  # global


def fa():
    a = 10  # local
    a += 1
    print(a)


print(a)  # Ex: 5
fa()  # Ex: 11
print(a)  # Ex: 5


def fa2():
    global a
    a += 1
    print(a)


print(a)  # Ex: 5
fa2()  # Ex: 6
print(a)  # Ex: 6


# Function in Function - funksiya ichida funksiya

l = [1, '2', 3]


def fl(l):  # Method - 1
    return [i * 2 for i in l]


print(fl(l))  # Ex: [2, '22', 6]


def fl2(l):  # Method - 2
    def get_mult(x):
        return int(x) * 2

    return [get_mult(i) for i in l]


print(fl2(l))  # Ex: [2, 4, 6]


def fl3(l):  # Method - 3
    def get_mult(x):
        if isinstance(x, int):
            return x * 2

    return [get_mult(i) for i in l if get_mult(i)]


print(fl3(l))  # Ex: [2, 6] no sting - sting olib tashlash


def fl4(l):  # Method - 4
    def get_mult(x):
        return x * 2
    return list(map(get_mult, l))


print(fl4(l))  # Ex: [2, '22', 6] no sting - sting olib tashlash
