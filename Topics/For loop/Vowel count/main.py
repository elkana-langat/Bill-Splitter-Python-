string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

number_of_vowels = 0

for letter in string:
    if letter in vowels:
        number_of_vowels += 1

print(number_of_vowels)