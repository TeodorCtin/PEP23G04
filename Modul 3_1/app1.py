#
#
# cnp = input('Introduceti primele 7 ciffe din cnp') #cnp = 1083456
#                                                     #     01234567
#
# an_curent = '2023'
#
# if cnp[1] == 0:
#     an_nastere = cnp[2]
#     varsta_user = int(an_curent[2:4]) - int(an_nastere)
#     # print(varsta_user)
#
#     if varsta_user > 18:
#         print('Aveti peste 18 ani')
#     elif varsta_user < 18:
#         print('Aveti sub 18 ani')
#
# elif cnp[1] != 0:
#     an_nastere = cnp[1:3]
#     varsta_user = int(an_curent[2:4]) - int(an_nastere)
#     # print(varsta_user)
#
#     if varsta_user > 18:
#         print('Aveti peste 18 ani')
#     elif varsta_user < 18:
#         print('Aveti sub 18 ani')
#
# elif cnp[1] > 2:
#     an_nastere = 1900 + int(cnp[1:3])
#     varsta_user = int(an_curent) - an_nastere
#     # print(varsta_user)
#
#     if varsta_user > 18:
#         print('Aveti peste 18 ani')
#     elif varsta_user < 18:
#         print('Aveti sub 18 ani')
#
#
#
# # varsta_user = int(an_curent[2:4]) - int(an_nastere)
# # # print(varsta_user)
# #
# # if varsta_user > 18:
# #     print('Aveti peste 18 ani')
# # elif varsta_user < 18:
# #     print('Aveti sub 18 ani')






curr_year = 2023
id = input('first 7 number from cnp: ')
if len(id) != 7:
    print('not enough characters')
else:
    year = int(id[1:3])
    print(year)
    if id[0] < '5':
        year += 1900
    else:
        year += 2000
    result = curr_year - year
    if result >= 18:
        print('Aveti peste 18 ani.')
    else:
        print('Nu aveti peste 18 ani')



