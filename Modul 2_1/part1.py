inaltime = input('Enter height: ')
baza = input('Enter base: ')
result = (int(inaltime) * int(baza)) / 2
print(type(result))
print('Area of the triangle is: ', result)


a = 10
b = 11
print('Memory location: ', id(a))
print('Memory location: ', id(b))
c = a + b
print('Memory location: ', id(c))
d = 21
print('Memory location: ', id(d))