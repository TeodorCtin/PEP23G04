import random

list_of_numbers = []
for i in range(1, 50):
    list_of_numbers.append(i)

server_choice = random.choices(list_of_numbers, k=6)

user_choice = []
while len(user_choice) < 6:
    try:
        option = int(input('Enter a number between 1 and 49:    '))
    except ValueError:
        print('You must introduce a number not a letter or special character')
        if ValueError:
            break
    while option not in list_of_numbers:
        try:
            option = int(input('Number must be between 1 and 49'))
        except ValueError:
            print('You must introduce a number not a letter or special character')
            if ValueError:
                break
        continue
    while option in user_choice:
        try:
            option = int(input('Numbers must be different:    '))
        except ValueError:
            print('You must introduce a number not a letter or special character')
            if ValueError:
                break
        continue

    user_choice.append(option)

print(server_choice)
print(user_choice)

list_of_correct_numbers_bulk = []
list_of_correct_numbers_cut = []


def choices_comparison():
    for a in server_choice:
        list_of_correct_numbers_bulk.append(a)
    for b in user_choice:
        list_of_correct_numbers_bulk.append(b)
    for c in list_of_correct_numbers_bulk:
        if c in list_of_correct_numbers_cut:
            continue
        else:
            list_of_correct_numbers_cut.append(c)

    if len(list_of_correct_numbers_cut) in range(1, 4):
        print(f'Congratulations! You \' ve guessed {list_of_correct_numbers_cut} numbers. You won 50 lei.')

    elif len(list_of_correct_numbers_cut) in range(4, 6):
        print(f'Congratulations! You \' ve guessed {list_of_correct_numbers_cut} numbers. You won 500 lei.')

    elif len(list_of_correct_numbers_cut) == 6:
        print(f'Congratulations! You \' ve guessed {list_of_correct_numbers_cut} numbers. You won 1500 lei.')
    else:
        print('Unfortunately, you haven\'t guessed any of the numbers. Good luck next time!')


choices_comparison()
