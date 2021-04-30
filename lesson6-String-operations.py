cc = 'C:\d\new.text'  # Ex:  --> \n pastga tushirvorishi XATOSI

print(cc)  # --> Ex: # C:\d
                     # ew.text

cd = r'C:\d\new.text'  # Ex: --> raw string \n pastga tushirvorishi XATOSINI TO'GIRLASH
print(cd)  # --> Ex C:\d\new.text

x = 'Hi '
print(x * 5)
"""

+---+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o |   | w | o | r | l | d | ! |
+---+---+---+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   9   10  11  12
-12 -11 -10 -9 -8  -7  -6  -5  -4  -3  -2  -1

[X:Y:Z]

"""
s = 'Hello world!'

# [X:Y:Z]
print(s[0:12])  # Ex: Hello world!
print(s[-1])  # Ex: !
print(s[0:5])  # Ex: Hello
print(s[:5])  # Ex: Hello
print(s[6:])  # Ex: world!
print(s[::2])  # Ex: Hlowrd
print(s[::-1])  # Ex: !dlrow olleH
print(s[:5] + s[6:])  # Ex: Helloworld!
