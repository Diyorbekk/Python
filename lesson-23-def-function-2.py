# Position Arguments - Biz ushbu funktsiyani ikkita argument bilan chaqirganimiz sababli, u muammosiz ishlaydi va bizda xato bo'lmaydi.
#
# Agar biz uni turli xil argumentlar bilan chaqirsak, interpreter xato haqida xabar beradi.Funksiyada nechta argument ishlatsak shuncha argument beliglab chaqirish kerak.
def position_args(a, b):
    return a + b


# --> print(position_args(1)) Ex: Error
print(position_args(1, 2))


# Keyword Arguments - Python sizga Keyword Arguments yordamida funktsiyalarni chaqirishga imkon beradi. Funktsiyalarni shu tarzda chaqirganimizda, argumentlarning tartibini (pozitsiyasini) o'zgartirish mumkin va standart holatini belgilashimiz va agar uni chaqirmasak u holda standart holatini belgilaydi.

def greet(name, msg=""):
    print("Hello", name + ', ' + msg)


greet("Bruce", msg="How do you do?")


# Keyword Arguments laridan keyingi Position Arguments xatolarga olib keladi.Agar funksiyada Position Argument mavjud bo'lsa unda Position Argument har doim birinchi bo'lib e'lon qilinadi.Agarda Position Argument mavjud bo'lib unda Position Argument oldin Keyword Arguments e'lon qilinsa xato qaytaradi.Masalan, funktsiya chaqiruvi quyidagicha ko'rinadi:
# --> greet(name="Bruce","How do you do?")  # SyntaxError: non-keyword arg after keyword arg


# Arbitrary Arguments - Ba'zan biz funktsiyaga o'tadigan argumentlar sonini oldindan bilmaymiz. Python Arbitrary Arguments bilan ko'plab argumentlar bilan chaqirish orqali kabi vaziyatlarni boshqarishimizga imkon beradi.
# Ular ikki xil ko'rinishda bo'ladi.
# 1. *args - Position Arguments - Tuples orqali qaytaradi.
# 2. **kwargs - Keyword Arguments - dict orqali qaytaradi.


def args_get(*args):
    print(args)


args_get(1, 4, 6, 10, 20, "hello")


def kwargs_get(**kwargs):
    print(kwargs)


kwargs_get(a=1, b=5, c=20)


# Argumentlar ning ketma-ketligi

def argument_get(a, x, *args, **kwargs):
    print(a, x, args, kwargs, sep='\n')


argument_get(1, 2, 3, 4, b=5, c=6)
