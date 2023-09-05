# first_number = int(input('give number:'))
#
# if first_number == 10:
#     print('number is 10')
# elif first_number == 11:
#     print('number is 11')
# elif first_number == 12:
#     print('number is 12')
# else:
#     print('number is other')

#
# a = 10
# print(a)
# a = a + 1
# print(a)
# a += 1
# print(a)
#
#
# while a >= 10:
#     print(a)
#     a -= 2
#
# print('Done')




#Example 1

# n = 0
#
# while n < 10:
#     if n == 7:
#         n += 1
#         continue
#     elif n == 8:
#         break
#     print(n)
#     n += 1


#Example 2
#
# a = 'abcd'
# done = 'done'
# if a:
#     print(done)
#
# print(bool('abcd'))
# print(bool('d'))
# print(bool(''))
#
#
# print(bool(100))
# print(bool(-100))
# print(bool(0))
#
# print(bool(None), 'is the values of None')
#
# if print('condition'):
#     print('failed')
# else:
#     print('success')

#Example 3

print(True and True)
print('x' and True)
print(True and 'x')

a = True
b = 'x'

if a:
    print(b)
else:
    print(a)