lista = input('Introduceti lista de taskuri: ')
lista_taskuri =lista.split(",")
# print(lista_taskuri)

lista_fara_dubluri = []

for element in lista_taskuri:
    if element not in lista_fara_dubluri:
        lista_fara_dubluri.append(element)
    elif element in lista_fara_dubluri:
        continue
print(lista_fara_dubluri)

