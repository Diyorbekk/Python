# Ex: Variable O'zgaruvchan ID Qaytatdan yaratadi
a = 10
print(a, id(a))  # 10
a = 20
print(a, id(a))  # 20


# Ex: String O'zgaruvchan ID Qaytatdan yaratadi
s = 'hello'
print(s, id(s))  # 'hello'
s += ' world'
print(s, id(s))  # 'hello world'


# Ex: List O'zgarmas ID Qaytatdan yaratmaydi
l = [1, 2, 3]
print(l, id(l))
l.append(5)
print(l, id(l))


# Ex: Integer O'zgaruvchan ID Qaytatdan yaratadi
x = 10
y = x
print(x, id(x))  # 10
print(y, id(y))  # 10
x = 15  # Qaytatdan yaratadi
print(x, id(x))  # 15
print(y, id(y))  # 10


# Ex: label "yorliq" O'zgarmas ID Qaytatdan yaratmaydi
l2 = [1, 2, 3]
l3 = l2

print(l2, id(l2))  # [1, 2, 3]
print(l3, id(l3))  # [1, 2, 3]

l2.append(5)
print(l2, id(l2))  # [1, 2, 3, 5]
print(l3, id(l3))  # [1, 2, 3, 5]


# Ex: label "yorliq" O'zgaruvchan ID Qaytatdan yaratadi
l4 = [1, 2, 3]
l5 = l4.copy()
# l5 = l4[:]

print(l4, id(l4))  # [1, 2, 3]
print(l5, id(l5))  # [1, 2, 3]

l4.append(5)
print(l4, id(l4))  # [1, 2, 3, 5]
print(l5, id(l5))  # [1, 2, 3]


# Ex: <Variable> O'zgaruvchini o'chirib tashashlash
delDelete = 100
print(delDelete)
del delDelete   # o'chirib tashashlash

