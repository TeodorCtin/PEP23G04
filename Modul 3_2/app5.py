password = 7788
entered_password = int(input('Introduceti parola: ').strip())
mistakes = 0
while mistakes < 3:
    mistakes += 1
    if entered_password == password:
        print('Acces permis')
        break
    else:
        entered_password = int(input(('Parola gresita. Mai incercati').strip()))