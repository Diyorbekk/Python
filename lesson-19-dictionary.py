d = {}  # empty dict - bo'sh dict


# Method 1
dict_1 = {'title': 'Sony', 'price': 100}


# Method 2
dict_2 = dict(title='Iphone', price=120)


# list to dict - list dan dict ga o'zgartirish
list_user = [
    ['bob@gmail.com', 'Bob'],
    ['katy@gmail.com', 'Katy'],
    ['john@gmail.com', 'John']
]
dict_3 = dict(list_user)


# tuples to dict - tuples dan dict ga o'zgartirish
tuple_user = (
    ('bob@gmail.com', 'Bob'),
    ('katy@gmail.com', 'Katy'),
    ('john@gmail.com', 'John')
)
dict_4 = dict(tuple_user)


# sets to dict - tuples dan dict ga o'zgartirish
sets_user = {1, 2, 3, 4, 5}
dict_5 = dict.fromkeys(sets_user, 0)


# The fromkeys() method returns a dictionary with the specified keys and the specified value. - Fromkeys() usuli dict belgilangan keys va belgilangan qiymat bilan qaytaradi.
dict_6 = dict.fromkeys(['price_1', 'price_2', 'price_2'], 50)


# dict in for - dict ichida for
dict_7 = {i: i + 1 for i in range(1, 10)}


dict_8 = [
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 110},
    {'title': 'Samsung', 'price': 90}
]

print(dict_1, dict_2, list_user, dict_3, tuple_user, dict_4, sets_user,
      dict_5, dict_6, dict_7, dict_8, sep='\n')
print()  # ajratish uchun


# --> print(dict_1['title2'])  # error
print(dict_1.get('title2', 'NO'))  # get - if no key - key bo'lmasa
print()  # ajratish uchun


# --> print(dict_7['1'])  # error string - string bilan yozish xato
print(dict_7[1])  # OK - number bilan yozish to'g'ri
print()  # ajratish uchun


# Method dict for - 1 - for orqali key ni va value (qiymatni) alohida ko'rish
for key in dict_1:
    print(f'{key}: {dict_1[key]}')
    # Example:
    # title: Sony
    # price: 100
print()  # ajratish uchun


# Method dict for - 2 - for orqali items() function bilan key ni va value (qiymatni) alohida ko'rish
for key, value in dict_1.items():
    print(key, value)
    # Example:
    # title Sony
    # price 100
print()  # ajratish uchun


# Method dict for - 3 - for orqali key ni va value (qiymatni) alohida ko'rish
for product in dict_8:
    print(product['title'],
          product['price'])
