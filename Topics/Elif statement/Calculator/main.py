# put your python code here
first_number = float(input())
second_number = float(input())
arithmetic_operation = input()


def multiplication(a, b):
    return a * b


def addition(a, b):
    return a + b


def division(a, b):
    return a / b


def subtraction(a, b):
    return a - b


def modula(a, b):
    return a % b


def power(a, b):
    return a ** b


def integer_div(a, b):
    return a // b


if arithmetic_operation == '+':
    print(addition(first_number, second_number))
elif arithmetic_operation == '-':
    print(subtraction(first_number, second_number))
elif arithmetic_operation == 'pow':
    print(power(first_number, second_number))
elif arithmetic_operation == '/':
    if second_number == 0:
        print("Division by 0!")
    else:
        print(division(first_number, second_number))
elif arithmetic_operation == '*':
    print(multiplication(first_number, second_number))
elif arithmetic_operation == 'mod':
    if second_number == 0:
        print("Division by 0!")
    else:
        print(modula(first_number, second_number))
elif arithmetic_operation == 'div':
    if second_number == 0:
        print("Division by 0!")
    else:
        print(integer_div(first_number, second_number))
