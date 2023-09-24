# print('---')
# print('| |')
# print('---')
#
# print('|----|')
# print('|    |')
# print('|----|')
#
#
#
# print('/', end = "")
# print('\\')
# print('--')
#
# print('()')

# my_list = [0, 1, 2, 3]
# x = 1
# for elem in my_list:
#     x = x * elem
# print(x)

# my_list = [1, 2, 3]
#           #0, 1, 2, 3
# for v in range(3):
#     my_list.insert(1, my_list[v])
# print(my_list)

# 3-0, 3-1, 3-2          0 t = [[3, 2, 1]
#                                      0      ]
# t = [[3-i for i in range (3)] for j in range (3)]
# s = 0
# for i in range(3):
#     s = s + t[i][i] #s = 6
# print(s)


# a  = 1
# b = 0
# c = a and b # c = 0
# d = a or b # d = 0
# e = a ** b # e = 1
#
#
# #1, 2, 3
# #-3, -2, -1

# my_list_1 = [1, 2, 3]
# my_list_2 = []
# for v in my_list_1:
#     my_list_2.insert(0, v)
# print(my_list_2)

# var = 1
# while var < 10:
#     print('#')
#     var = var << 1

# var = 0
# while var < 6:
#     var = var + 1
#     if var % 2 == 0:
#         continue
#     print('#')
#
# x = 1
# x = x == x
# print(x)
#
# # [0, 1, 2, 3]
# # [0, 1      ]
#
# vals = [0, 1, 2]
# vals.insert(0, 1)
# del vals[1]


# def enter_a_value(a):
#     pass
#
# for i in range(3):
#     enter_a_value(int(input("Please, enter a value:      ")))

# def boring_function():
#     print("'Boredom Mode' ON.")
#     return 123
#
# print("This lesson is interesting!")
# boring_function()
# print("This lesson is boring...")
#
# burh = []
# burh.insert(0, 7)


my_list = ['Mary', 'had', 'a', 'little', 'lamb']

# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'
#
# print(my_list(my_list))

# lst = [[x  for x in range (3)] for y in range (3)]
#
# for r in range (3):
#     for c in range (3):
#         if lst[r][c] % 2 != 0:
#             print('#')

# my_list = [x *  x for x in range(5)]
#
# def fun(lst):
#     del lst[lst[2]]
#     return lst
#
# print(fun(my_list))
#
# print(1//2)

# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)
#
# nums = [1, 2, 3]
# vals = nums
# del vals[:]
# print(vals, " ", nums)
#
# print( 1 // 5 + 1 / 5)


# x = float(input())
# y = float(input())
# print(y ** (1 / x))

#
# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)
#
# for x in dct.keys():
#     print(dct[x][1], end="")

x = "hello"

# if condition returns True, then nothing happens:
assert x == "hello"

# if condition returns False, AssertionError is raised:
assert x == "goodbye"
