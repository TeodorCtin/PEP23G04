#Method 1

user_string = input('Enter a string: ')
string_length = len(user_string)
string_length_output = 'Lungimea stringului este: {}'
string_length_output = string_length_output.format(string_length)
print(string_length_output)

#Method 2

user_string = input('Enter a string: ')
string_length = len(user_string)
string_length_output = f'Lungimea stringului este: {string_length}'
print(string_length_output)


#Method 3

user_string = input('Enter a string: ')
string_length = len(user_string)
print("Lungimea stringului este: " + str(string_length))

#Method 4

user_string = input('Enter a string: ')
string_length = len(user_string)
print('Lungimea stringului este: ', str(string_length))