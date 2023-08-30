
my_added_string = 'add me'

string1 = u'Hello World\n' #u = unicode, varianta default

string2 = r'Hello World\n' #r = raw

string3 = '''




Hello World



''' #stringul poate fi scris pe mai multe linii

string4 = f'Hello World {my_added_string}'

string5 = rf"\nHello World {my_added_string}" #raw si formated

print(string1, string2, string3, string4, string5, sep = '\t')

string4 = f'Hello World' #string formatabil


string5 = rf"\nHello World {my_added_string}" #raw si formated

string_with_quotes = 'my string \''
print(string_with_quotes)

#String methods

my_string = 'Hello World, {}'
my_string = my_string.format('Python')
print(my_string)


my_string = 'Hello World, {1} {0}'
my_string = my_string.format('Python', 'User')
print(my_string)


my_string = 'Hello World, {arg1} {arg2}'
my_string = my_string.format(arg1 = 'Python', arg2 = 'User')
print(my_string)

print(len(my_string))


print('___'.center(11, '#'))

my_string = 'Hello World'
print(my_string[0])
print(my_string[len(my_string) - 1])
print(my_string[-1])


#'HelloWorld'
#0123456789

print(my_string[0:3])
print(my_string[-1:-5])