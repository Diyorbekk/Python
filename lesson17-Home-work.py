# Task - 1
words = ['мадам', 'топот', 'test', 'madam', 'word']

# Method 1
palindromes = [word for word in words if word == word[::-1]]
print(palindromes)

# Method 2
palindromes_Method_2 = []

for word in words:
    if word == word[::-1]:
        palindromes_Method_2.append(word)

print(palindromes_Method_2)


# Task - 2
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
palindromes = []
for word in my_str:
    word_r = word.replace(' ', '').lower()
    if word_r == word_r[::-1]:
        palindromes.append(word)
print(palindromes)


# New Function - Yengi Funksiya

# Join and Map
l1 = list(range(1, 10))
dots = '..'.join(map(str, l1))  # Add dots using join as a number string through the map - Map orqali number string qilib join yordamida dots qo'shish

l2 = list('hello')
line = '-'.join(l2)  # Add a line using Join - Join yordamida line qo'shish


print(dots, line, sep='\n')


