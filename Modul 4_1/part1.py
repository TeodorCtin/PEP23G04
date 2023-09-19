# result = 'a'
#
#
# def factorial(number):
#     global result
#     print('in function', result)
#     result = 1
#     for i in range(1, number + 1):
#         result *= i
#     return result
#     # return True
#     print('last print: ', result) # this will never get executed
#
#
# returnet_result = factorial(5)
# print('outside function', result)
# print(returnet_result)

t1 = tuple('abc')


print(t1)

print(t1[0])
print(t1[0:2])

t2 = 1, 2, 3, 4
print(t2)

a = 1
b = 2

a, b = b, a
print(a, b)

tuple_with_vars = (a, b)


print(tuple_with_vars[0], '->', tuple_with_vars[1])