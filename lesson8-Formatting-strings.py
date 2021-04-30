name = "Diyor"
age = 22


# Old Version Python Formatting. Eski Versiyadagi Python Formatlash

print('My name is ' + name + '. I\' ' + str(age))  # Old Version Python Formatting. Eski Versiyadagi Python Formatlash    Ex: My name is Diyor. I' 22
print('My name is %(name)s. I\' %(age)d' % {'name': name, 'age': age})  # Old Version Python Formatting. Eski Versiyadagi Python Formatlash   // Nomlash orqali Formatlash    Ex: My name is Diyor. I' 22
print('My name is %s. I\' %d' % (name, age))  # Old Version Python Formatting. Eski Versiyadagi Python Formatlash   // Kettma-kettlik orqali Formatlash     Ex: My name is Diyor. I' 22
print('Title: %s, Price: %f' % ('Sony', 40))  # Old Version Python Formatting. Eski Versiyadagi Python Formatlash   // Belgilash usulda Kettma-kettlik orqali Formatlash    Ex: Title: Sony, Price: 40.000000
print('Title: %s, Price: %.2f' % ('Sony', 40))  # Old Version Python Formatting. Eski Versiyadagi Python Formatlash   // Belgilash usulda number ni kichiklash Kettma-kettlik orqali Formatlash  Ex: Title: Sony, Price: 40.00

# New Python 3.0 Up Version Formatting. Yangi Python 3.0 katta Versiyadagi Formatlash

print('My name is {}. I\'m {}'.format(name, age))   # Kettma-kettlik orqali Formatlash     Ex: My name is Diyor. I' 22
print('My {1} name is {0}. I\'m {1}'.format(name, age))   # number lash orqali Formatlash     Ex: My 22 name is Diyor. I'm 22
print('My {age} name is {name}. I\'m {age}'.format(name=name, age=age))   # nomlash lash orqali Formatlash     Ex: My 22 name is Diyor. I'm 22

# New Python 3.5 Up Version Formatting. Yangi Python 3.5 katta Versiyadagi Formatlash
# f-strings

print(f'My name is {name}. I\'m {age}')    # f-stings orqali Formatlash     Ex: My name is Diyor. I' 22
print(f'My name is {name}. I\'m {age + 4}')    # f-stings qo'shimcha qo'shish orqali Formatlash     Ex: My name is Diyor. I'm 26
print(f'My name is {name}. I\'m {age + age}')    # f-stings qo'shimcha qo'shish orqali Formatlash     Ex: My name is Diyor. I'm 44
