import random

defValue = random.randint(1, 100)

for i in range(1, 4):
    print(f'{i} - urunush')
    vote = int(input('Soni kiriting '))
    if defValue < vote:
        print(f'{vote} dan kam')
    elif defValue > vote:
        print(f'{vote} dan ko\'p')
    elif defValue == vote:
        print(f"Siz {i} urunishda toptingiz")
        break

else:
    print(f'siz toplomadingiz javobi {defValue}')
