# Tuples bir nechta elementni bitta o'zgaruvchida saqlash uchun ishlatiladi.
# Tuple - bu buyurtma qilingan va o'zgarmas to'plam.

t = (1, 2, 3)  # tuple()
l = [1, 2, 3]  # list()
t1 = 1, 2, 3  # tuple no recommended - Tavsiya etilmaydi

t2 = tuple((1, 2, 3))  # tuple() group number - Gruppalash
t3 = ()  # empty tuple() - Bo'sh
t4 = (1,)  # tuple one element - Bitta element
t5 = tuple('hello')  # tuple string
t6 = t.__sizeof__()  # tuple size  48   Recommended - Tavsiya etiladi.Kam joyni
t7 = l.__sizeof__()  # list size  104   Ko'p joyni egallaydi

t8 = tuple('hello')
t9 = tuple(' world')
t10 = t8 + t9  # adding tuple - Qo'shish

t11 = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])  # tuple id - id raqami

print(t, l, t1, t2, t3, t4, t5, t6, t7, t10, len(t10), t11, id(t11), sep='\n')
t11[4][0] = 'new'  # tuple change element - elementni o'zgartirish
t11[4].append('hello')  # tuple adding element = element qo'shish
print(t11)

t12 = (1, 2, 3)  # adding variables - o'zgaruvchalariga qo'shish
x, y, z = t12
print(x, y, z)

# element change position - elementning positsiyasini o'zgatirish
a = 1
b = 2
print(a, b)
a, b = b, a
print(a, b)


for i in t10:
    if i == ' ':
        continue
    print(f'"{i}"', end=' ')
