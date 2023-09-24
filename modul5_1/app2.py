lst = []
while True:
    numar = input("Introduceti un numar (cand v-ati saturat,apasati q): ")
    if numar == 'q':
        break
    numar = int(numar)
    lst.append(numar)
# Suma numarului de pe pozitia 1 si 2.
print("O sa adaugam numarul de pe pozitia 2 si cel de pe pozitia 3.")
# print("lst[1] + lst[2] = ", lst[1] + lst[2])
try:
    print("lst[1] + lst[2] = ", lst[1] + lst[2])
except IndexError:
    print('Nu ai introdus suficiente numere')
# Divizia primelor 2 numere din lista
print("Divizia primelor 2 numere din lista este: ")
# print("lst[0] / lst[1] = ", lst[0] / lst[1])
try :
    print("lst[0] / lst[1] = ", lst[0] / lst[1])
except ZeroDivisionError:
    print('Divizia nu e poate face la 0')


# Suma tuturor numerelor din lista
sum = 0
for i in lst:
    sum += i
print("Suma tuturor numerelor din lista este: ", sum)