# put your python code here
string_alphabet = 'abcdefghijklmnopqrstuvwxyz'
list_alphabet = list(string_alphabet)
double_list_alphabet = []
for letter in list_alphabet:
    double_list_alphabet.append(letter * 2)

double_alphabet = dict.fromkeys(list_alphabet)

i = 0
for key in double_alphabet:
    double_alphabet[key] = double_list_alphabet[i]
    i += 1
