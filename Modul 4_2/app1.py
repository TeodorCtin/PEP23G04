def sondaj(number_of_participants):
    ages = {}
    sum_of_ages = 0
    for i in range( number_of_participants):
        age = int(input(f'Introduceti varsta participantului {i + 1}:   '))
        ages[i] = age
        sum_of_ages += age
    arithmetic_average = sum_of_ages/number_of_participants
    print(f'Media de varsta este {arithmetic_average}')


# print(ages)

sondaj(number_of_participants = int(input('Cati participanti avem astazi?   ')))
