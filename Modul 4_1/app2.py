number = input('Introduceti un numar')
result = int(number)


def calculate(number):
    global result
    result = result ** int(number)
    print(result)


condition = True
while condition:
    number = input('Introduceti un numar')
    if number == 'q':
        condition = False
        continue
    calculate(int(number))
