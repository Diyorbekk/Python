x = 5

# Ikkala operand tengligini tekshiradi. Agar ha bo'lsa, unda shart to'g'ri bo'ladi.

if x == 5:        # Agar x teng bo'lsa 5 ga
    print("To'g'ri Bo'lsa")


# Ikkala operand tengligini tekshiradi. Agar yo'q bo'lsa, unda shart to'g'ri bo'ladi.


if x != 5:      # Agar x teng bo'lmasa 5 ga
    print("To'g'ri Bo'lmasa")


# Esle ni tekshirish


if x == 5:          # Agar x teng bo'lsa 5 ga
    print("To'g'ri Bo'lsa")

elif x != x:        # Agar x teng bo'lmasa x ga
    print("Else ni tekishirsh uchun")
else:               # Agar da shartlar to'g'ri kelmasa
    print("Agar da shartlar to'g'ri kelmasa")


# Chap operandning qiymati o'ngnikidan kattaroqligini tekshiradi. Agar ha bo'lsa, unda shart to'g'ri bo'ladi.


if x > 2:           # Agar x 2 dan ko'p bo'lsa True
    print(f"{x} 2 dan ko'p")
else:
    print("Agar da shartlar to'g'ri kelmasa")


# Chap operandning qiymati o'ngnikidan kattaroq yoki tengligini tekshiradi. Agar ha bo'lsa, unda shart to'g'ri bo'ladi.


if x >= 5:  # Agar x 5 dan ko'p yoki teng bo'lsa True
    print(f'{x} 5 ga teng')
else:
    print("Agar da shartlar to'g'ri kelmasa")


# Chap operandning qiymati o'ngning qiymatidan kichikligini tekshiradi. Agar ha bo'lsa, unda shart to'g'ri bo'ladi.


if x < 2:          # Agar x 2 dan kam bo'lsa False
    print(f'{x} 2 dan kam')

else:
    print("Agar da shartlar to'g'ri kelmasa")


# Chap operandning qiymatini o'ng operandning qiymatidan kamroq yoki tengligini tekshiradi. Agar ha bo'lsa, unda shart to'g'ri bo'ladi.


if x <= 5:         # Agar x ko'p yoki teng 5 ga bo'lsa True
    print(f'{x} 5 ga teng')
else:
    print("Agar da shartlar to'g'ri kelmasa")


# Python-dagi bitli operatorlar:
# Bitwise operatorlari bit (ikkilik) formatdagi ma'lumotlar bilan ishlashga mo'ljallangan. Aytaylik, bizda ikkita raqam bor a = 60; va b = 13. Ikkilikda ular quyidagicha bo'ladi:


a = 60
# a = 0011 1100
b = 13
# b = 0000 1101


# Ikkilik "AND" operatori, bit ikkala operandada mavjud bo'lgan taqdirdagina, natijaga bitni ko'chiradi.


if a & b:
    print(a & b)   # (a & b) bizga 12 beradi, ikkilikda 0000 1100 ga o'xshaydi


# Ikkilik "OR" operatori, agar u kamida bitta operandda bo'lsa, biroz nusxa ko'chiradi


if a | b:
    print(a | b)   # (a | b) bizga 61, ikkilik 0011 1101 da beradi


# Ikkilik "Eksklyuziv YOKI" operatori bit faqat operandalarning birida mavjud bo'lgan taqdirda, lekin ikkalasida ham birdaniga bo'lmaganda nusxa ko'chiradi.


if a ^ b:
    print(a ^ b)   # (a ^ b) bizga 49, ikkilik 0011 0001 da beradi


# Ikkilik bepul operator. Unary (ya'ni bitta operand kerak) bitlarni teskari yo'naltiradi, u erda bittasi nolga teng bo'ladi va aksincha.


if ~a:
    print(~a)   # (~ a) -61 ga olib keladi, ikkilikda 1100 0011 ga o'xshaydi.


# Bitta chapga siljish. Chap operandning qiymati o'ng operandda ko'rsatilgan bitlar soniga chapga "siljiydi".


if a << 2:
    print(a << 2)  # a << 2 natijasi 240 ga, ikkilik 1111 0000 ga teng bo'ladi


# O'ngga siljish. Chap operandning qiymati o'ng operandda ko'rsatilgan bitlar soni bo'yicha o'ngga "siljiydi".

if a >> 2:
    print(a >> 2)   # a >> 2  15 ni beradi, ikkilikda 0000 1111


# Python-da mantiqiy operatorlar:


if x and x:
    print("True")   # Mantiqiy va operator. Ikkala operand ham to'g'ri bo'lsa, shart to'g'ri bo'ladi.
# True and True teng True.
# True and False teng False.
# False and True teng False.
# False and False teng False.


if x or x:
    print("True")   # "OR" mantiqiy operatori. Agar operandlarning kamida bittasi to'g'ri bo'lsa, unda butun ifoda to'g'ri bo'ladi.
# True or True teng True.
# True or False teng True.
# False or True teng True.
# False or False teng False.


if not x:
    print("False")  # "YO'Q" mantiqiy operatori. Operandning mantiqiy qiymatini o'zgartiring.
# not True teng False.
# not False teng True.
