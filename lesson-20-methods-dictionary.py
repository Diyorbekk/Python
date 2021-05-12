dict_product_1 = {'title': 'Sony', 'price': 100}


# keys() - dict keys larni qaytaradi
print(dict_product_1.keys())
# Ex: dict_keys(['title', 'price'])


# get(key[, default]) - keys ning qiymatini qaytaradi, lekin agar u mavjud bo'lmasa, u istisno qilmaydi, lekin standartni qaytaradi (standart None)
print(dict_product_1.get('title2', 'None'))
# Ex: None


# copy() - dict ning nusxasini qaytaradi
dict_product_1_copy = dict_product_1.copy()
print(dict_product_1_copy)
# Ex: {'title': 'Sony', 'price': 100}


# clear() - dict ni tozalaydi
dict_product_1_copy.clear()
print(dict_product_1_copy)
# Ex: {}


# items() - dict ni juftlarni qaytaradi (keys, value)
print(dict_product_1.items())
# Ex: dict_items([('title', 'Sony'), ('price', 100)])


# pop(key[, default]) - keys olib tashlaydi va qiymatni qaytaradi. Agar keys bo'lmasa, standart qiymatni qaytaradi (standart istisno)
print(dict_product_1.pop('title2', 'NO'))
# Ex: NO
# --> print(dict_product_1.pop('title_2'))
# Ex_Standart: KeyError: 'title_2'
# --> print(dict_product_1.pop('title'))
# Ex_Pop_element: Sony
# --> print(dict_product_1)
# Ex_dict: {'price': 100}


# update() - dict ni boshqa dict ob'ekti yoki takrorlanadigan keys / value juftliklari elementlari bilan yangilaydi.
dict_product_1.update({'price': 200})
print(dict_product_1)
# Ex_element_update: {'title': 'Sony', 'price': 200}
dict_product_1.update({'price_2': 1200})
# Ex_new_element_update: ('price_2', 1200)
print(dict_product_1)
# Ex: {'title': 'Sony', 'price': 200, 'price_2': 1200}


# Popitem() - usuli (keys, value) juftligini lug'atdan oxiridan birinchi tartibda olib tashlaydi va qaytaradi.
dict_pop_item = dict_product_1.popitem()
print(dict_product_1, dict_pop_item, sep='\n')
# Ex: {'title': 'Sony', 'price': 200}


# setdefault(key[, default]) - keys qiymatini qaytaradi, ammo agar u mavjud bo'lmasa, u istisno qilmaydi, lekin standart qiymati bilan keys yaratadi (standart None)\
print(dict_product_1.setdefault('title-2'))
# Ex_Standart:  None
print(dict_product_1.setdefault('title_2', 'Panasonic'))
# Ex: Panasonic
print(dict_product_1)
# Ex: {'title': 'Sony', 'price': 200, 'title-2': None, 'title_2': 'Panasonic'}

# values() - dict dagi value ni qaytaradi
print(dict_product_1.values())
# Ex: dict_values(['Sony', 200, None, 'Panasonic'])



