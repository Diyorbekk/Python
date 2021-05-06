# Set - bu ma'lumotlar to'plamini saqlash uchun ishlatiladigan Python-dagi o'rnatilgan 4 ta ma'lumot turlaridan biri, qolgan 3 tasi "List", "Tuple" va "Dictionary", ularning barchasi har xil sifat va foydalanishga ega.
# Set - bu tartibsiz va indekslanmagan to'plam.
# Set - bir xil qiymatga ega ikkita element birini olib tashlaydi.


set_1 = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}  # Method - 1 = Set tartibsiz, shuning uchun elementlarning qaysi tartibda paydo bo'lishiga amin bo'lmaysiz. Bir xil qiymatga ega ikkita element birini olib tashlaydi.
set_2 = set(('apple', 'orange', 'apple', 'pear', 'orange', 'banana'))  # Method - 2
set_3 = {i for i in range(1, 11)}  # Method - 3
set_4 = set()  # Method - 4 Empty set

l_1 = list(range(1, 11))
set_5 = set(l_1)  # Method - 5
set_6 = list(set(l_1))  # Method - 6 To list

print(set_1, set_2, set_3, set_4, set_5, set_6, sep='\n')

a = set('abracadabra')
b = set('alacazam')


set_7 = a - b  # set_7 = set.difference(a, b)  # Method - 7 ayirish - b qatoridagi a dagi harflarini olib tashlash   Ex: {'r', 'd', 'b'}
set_8 = a | b  # set_8 = set.union(a, b)  # Method - 8 birlashma - a yoki b dagi harflar birlashmasi   Ex: {'a', 'm', 'c', 'z', 'b', 'r', 'l', 'd'}
set_9 = a & b  # set_9 = set.intersection(a, b)  # Method - 9 kesishma - ikkala a va b harflaridagi olib tashlanganlar to'plami   Ex: {'a', 'c'}
set_10 = a ^ b  # set_10 = set.symmetric_difference(a, b)  # Method - 10 elementlar to'plami - ikkala a va b harflaridagi olib tashlangan to'plami   Ex: {'r', 'l', 'z', 'd', 'b', 'm'}

# set.copy() - Set nusxasini qaytaradi
# set.add(elem) - Set ga element qo'shadi
# set.remove(elem) - Set dan elementni olib tashlaydi. Agar bunday element mavjud bo'lmasa, KeyError
# set.discard(elem) - agar u Set da bo'lsa, elementni olib tashlaydi
# set.pop() - qaytaradi va Set dan birinchi elementni olib tashlaydi. Set larga buyurtma berilmaganligi sababli, qaysi mahsulot birinchi bo'lishini aniq aytish mumkin emas --> # Set - bu tartibsiz va indekslanmagan to'plam.
# set.clear() - Set ni tozalash

print(a, b, set_7, set_8, set_9, set_10, sep='\n')

# Set va frozenset o'rtasidagi yagona farq shundaki, bu Set <<O'zgaruvchan ma'lumotlar turi>>, ammo frozenset bunday emas <<O'zgarmas>>.!!! Frozenset da qo'shish,o'chirish va o'zgartirish mumkun emas !!!.

a_frozenset = frozenset('hello')
a_frozenset.add(b)  # AttributeError: 'frozenset' object has no attribute 'add' - AttributeError: 'frozenset' ob'ektida 'add' atributi yo'q
print(a_frozenset)
