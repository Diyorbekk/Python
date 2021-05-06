# Home Work Lesson-10-For-While
year = 1900
while year <= 2021:
    year += 1
    print(year)
else:
    print("Done")


# Ex: 1 simply
l = [1, 2, 3, 'hello', ['test', 10], 'world', True]


# Ex: 2 list(string)
l2 = list('hello')


# Ex: 3 list(number)
l3 = list((1, 2, 3))

# Ex: 4 for
l4 = [i for i in 'hello']


# Ex: 5 for in
# l5 = [i for i in 'hello world' if i != ' ' and i != 'e']
l5 = [i for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]


# Ex: 6 list range
l6 = list(range(0, 11))

print(l, l2, l3, l4, l5, l6, sep='\n')

# Ex: 7 for in for
for i in range(1, 3):
    print(f'Tashqi sikl #{i}')
    for j in range(1, 3):
        print(f'\t Ichki sikl #{j}')




