import random

name = input('Introduceti numele')
server_name = 'Server'

list_of_options = ['piatra', 'hartie', 'foarfeca']

user_choice = input('Introduceti optiunea: p (piatra), f( foarfeca), h (hartie)')
server_choice = random.choice(list_of_options)


def verificare_optiuni():
    if (server_choice == 'piatra' and user_choice == 'piatra') or (
            server_choice == 'hartie' and user_choice == 'hartie') or (
            server_choice == 'foarfeca' and user_choice == 'foarfeca'):
        print(f'{name}: {user_choice} \n {server_name}: {server_choice} \n Egalitate!')

    if (server_choice == 'piatra' and user_choice == 'hatrie') or (
            server_choice == 'foarfeca' and user_choice == 'piatra') or (
            server_choice == 'hartie' and user_choice == 'foarfeca'):
        print(f'{name}: {user_choice} \n {server_name}: {server_choice} \n {name}, ai castigat!')

    if (server_choice == 'piatra' and user_choice == 'foarfeca') or (
            server_choice == 'foarfeca' and user_choice == 'hartie') or (
            server_choice == 'hartie' and user_choice == 'piatra'):
        print(f'{name}: {user_choice} \n {server_name}: {server_choice} \n {server_name}, ai castigat!')


if user_choice == 'p':
    user_choice = 'piatra'
    verificare_optiuni()
elif user_choice == 'f':
    user_choice = 'foarfeca'
    verificare_optiuni()
elif user_choice == 'h':
    user_choice = 'hartie'
    verificare_optiuni()
else:
    print('Optiune invalida')
