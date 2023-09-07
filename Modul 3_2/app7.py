word = input('Introduceti un cuvant ( fara majuscule ): ').strip()

for letter in word:
    break
print(letter)

letter_counter = 0

for letter_match in word:
    if letter_match == letter:
        letter_counter += 1
        continue

print(f'Litera {letter} se repeta de {letter_counter} ori')
