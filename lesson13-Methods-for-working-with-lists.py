l = [1, 2, 3, 'hello', ['test', 10], 'world', True]
names = ['Ivanov', 'Petrov', 'Sidorov']

# Ex 1 append
l.append(4)  # Ro'yxat oxiriga element qo'shadi   --> [1, 2, 3, 'hello', ['test', 10], 'world', True, 4]


# Ex 2 extend
l.extend([7, 8])  # L ning barcha elementlarini oxirigacha qo'shib ro'yxatni kengaytiradi   --> [1, 2, 3, 'hello', ['test', 10], 'world', True, 4, 7, 8]
l.extend(names)  # L ning barcha elementlarini oxirigacha qo'shib ro'yxatni kengaytiradi    --> [1, 2, 3, 'hello', ['test', 10], 'world', True, 4, 7, 8, 'Ivanov', 'Petrov', 'Sidorov']

# Ex 3 insert
l.insert(2, 'new position element')  # index positsiya-elementga x qiymatini kiritadi    --> [1, 2, 'new position element', 3, 'hello', ['test', 10], 'world', True, 4, 7, 8, 'Ivanov', 'Petrov', 'Sidorov']

# Ex 4 remove
l.remove('new position element')  # Ro'yxatdagi x qiymatiga ega bo'lgan birinchi elementni olib tashlaydi. Agar bunday element mavjud bo'lmasa ValueError    --> [1, 2, 3, 'hello', ['test', 10], 'world', True, 4, 7, 8, 'Ivanov', 'Petrov', 'Sidorov']

# Ex 5 pop
l2 = l.pop(3)  # l-elementni olib tashlaydi va uni qaytaradi. Agar indeks ko'rsatilmagan bo'lsa, oxirgi element o'chiriladi
print(l, l2, sep='\n')  # [1, 2, 3, ['test', 10], 'world', True, 4, 7, 8, 'Ivanov', 'Petrov', 'Sidorov']
                        # hello


# Ex 6 index
l3 = l.index('world')  # Birinchi elementning index holatini x qiymatiga qaytaradi (boshidan oxirigacha qidirish paytida)
print(l, l3, sep='\n')  # [1, 2, 3, ['test', 10], 'world', True, 4, 7, 8, 'Ivanov', 'Petrov', 'Sidorov']
                        # 4


# Ex 7 count
l4 = l.count('world')  # X qiymati bo'lgan elementlar sonini qaytaradi
print(l, l4)  # [1, 2, 3, ['test', 10], 'world', True, 4, 7, 8, 'Ivanov', 'Petrov', 'Sidorov']
              # 1


# Ex 8 sort
nameSort = ['Diyor', 'Abduqodir', 'Jasur', 'Begzod', 'Elmurod']
nameSort.sort()  # Ro'yxatni Alfavit funktsiyasiga qarab saralaydi
print(nameSort)

# Ex 9 reverse
nameReverse = ['Diyor', 'Abduqodir', 'Jasur', 'Begzod', 'Elmurod']
nameReverse.reverse()  # Ro'yxatni teskari yo'naltiradi.    --> ['Elmurod', 'Begzod', 'Jasur', 'Abduqodir', 'Diyor']
print(nameReverse)


# Ex 10 copy
l5 = l.copy()  # Ro'yxatning nusxasi    --> [1, 2, 3, ['test', 10], 'world', True, 4, 7, 8, 'Ivanov', 'Petrov', 'Sidorov']
print(l5)


# Ex 11 clear

l5.clear()  # Ro'yxatni tozalaydi   --> []
print(l5)
