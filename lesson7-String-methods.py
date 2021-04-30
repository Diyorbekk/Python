

s = "hello, world"

# print(len(s))  # index bilib olish?

print(s.find('e'))  # index bo'yicha qidirish.Birinchi voqea sonini qaytaradi yoki -1

print(s.rfind('e'))  # index bo'yicha qidirish.Oxirgi voqea sonini qaytaradi yoki -1

print(s.index('e'))  # index bo'yicha qidirish.Birinchi voqea sonini qaytaradi yoki Xato bo'lib qaytadi

print(s.rindex('e'))  # index bo'yicha qidirish.Oxirgi voqea sonini qaytaradi yoki Xato bo'lib qaytadi

print(s.replace('l', 't'))  # index bo'yicha qidirish.Shablonni almashtirish uchun almashtirish.     Ex: hetto

print(s.replace('l', 't', 1))  # index bo'yicha qidirish.Shablonni almashtirish uchun almashtirish. maksimal hisoblash almashtirishlar sonini cheklaydi.  Ex: hetlo

print(s.split())  # Bo'inishi ajratuvchi bilan ajratish     Ex: ['hello,', 'world']

print(s.split(','))  # Bo'inishi ajratuvchi bilan ajratish     Ex: ['hello', ' world']

print(s.isdigit())  # Agar Stringi ichida number bor bo'sa True bo'lmasa False qaytadi.      Ex: False

print(s.isalpha())  # Agar Stringi ichida to'liq harflar bor bo'sa True bo'lmasa (symbol va probel bo'lsa False qaytadi) False qaytadi.      Ex: False

print(s.isalnum())  # Agar Stringi ichida to'liq harflar va number bor bo'sa True bo'lmasa (symbol va probel bo'lsa False qaytadi) False qaytadi.      Ex: False

print(s.isalnum())  # Agar Stringi ichida to'liq hammasi kichik harflar bo'sa True bo'lmasa (symbol va probel bo'lsa False qaytadi) False qaytadi.      Ex: False

print(s.isupper())  # Agar Stringi ichida to'liq hammasi katta harflar bo'sa True bo'lmasa (symbol va probel bo'lsa False qaytadi) False qaytadi.      Ex: False

print(s.capitalize())  # Bosh harfni kattada qoganlarini kichik harflarda qiladi.      Ex: Hello, world

print(s.center(20))  # To'ldirilgan holda markazlashtirilgan qatorni qaytaradi (пробел по умолчанию)       Ex:    hello, world

print(s.center(20, "!"))  # To'ldirilgan holda markazlashtirilgan qatorni qaytaradi (пробел по умолчанию)       Ex: !!!!hello, world!!!!

print(s.count("l"))  # [Start, end] (0 va standart satr uzunligi) oralig'ida substringning bir-birining ustiga chiqmaydigan takrorlanish sonini qaytaradi.   Ex: 3

print(s.strip())  # Satr boshida va oxirida bo'sh joyni olib tashlash.Yana kerekmas hosalarini olib tashlaydi.
