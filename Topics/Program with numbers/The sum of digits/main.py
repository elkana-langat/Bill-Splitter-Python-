# put your python code here
number = int(input())
last_digit = number % 10

new_number = number // 10

second_digit = new_number % 10
first_digit = number // 100

print(sum([last_digit, second_digit, first_digit]))
