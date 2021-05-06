i = 1
while i <= 10:
    print(i)
    i += 1


print("Hello", "world", sep='!', end=' | ')
# Ex: Hello!world |
print("Hello 2", "world 2")
# Ex: Hello!world | Hello 2 world 2


s = 'Hello world'
for l in s:
    if l == ' ':
        continue
# Ex: H e l l o w o r l d
    print(l, end=" ")  # Ex: Helloworld!
# Ex: H e l l o   w o r l d


for j in 'Hello world':
    if j == ' ':
        break
    print(j)
# Ex: Hello


for v in 'Helloworld':
    if v == ' ':
        break
    print(v, end=' ')
else:
    print("\nNo space")
# Ex: H e l l o w o r l d
# No space

