nume_elev = input('Introduceti numele elevului:    ')

note = input(f'Introduceti notele elevului {nume_elev}:    ').split(',')


def medie_elev():
    suma = 0
    for i in note:
        try:
            suma += int(i)
        except ValueError:
            print('Trebuie sa introduci doar valori numerice cuprinse intre 1 si 10')
            return
    medie_aritmetica = suma / len(note)
    # print(len(note))
    print(medie_aritmetica)
    if medie_aritmetica < 5:
        print(f'Elevul {nume_elev} a picat clasa')
    elif medie_aritmetica >= 5:
        print(f'Elevul {nume_elev} a trecut clasa')
    return medie_aritmetica


medie_elev()
