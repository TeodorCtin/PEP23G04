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

var = 0
while var < 6:
    var = var + 1
    if var % 2 == 0:
        continue
    print('#')

x = 1
x = x == x
print(x)

# [0, 1, 2, 3]
# [0, 1      ]

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]