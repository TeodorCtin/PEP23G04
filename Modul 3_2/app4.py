options = [1, 2]
choices = [4, 3.5]
currency = [5, 10]

print('1. Capuccino ... 4 lei')
print('2. Espresso ... 3.5 lei')
choice = int(input('Ce optiune alegeti? [1:2]: ').strip())
money = int(input('Introduceti o bancnota [5, 10]: ').strip())
if money in currency:
    if choice in options:
        print(f'Veti primi restul de {money - choices[choice - 1]} lei')
    else:
        print('Optiune invalida')
else:
    print('Bancnota incorecta')

# if choice == '1'and money == '5':
#     print('Veti primi restul de 1 lei')
#
# if choice == '1' and money == '10':
#     print('Veti primi restul de 6 lei')
#
# if choice == '2' and money == '5':
#     print('Veti primi restul de 1.5 lei')
#
# if choice == '2' and money == '10':
#     print('Veti primi restul de 6.5 lei')