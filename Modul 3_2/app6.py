list = ['Masa', 5, 'Scaun', 4.5, [5, 6, 7], 8]

for obiect in list:
    var_type = str(type(obiect)).split("\'")[1]
    print(f'Tipul obiectului {obiect} este {var_type}')
