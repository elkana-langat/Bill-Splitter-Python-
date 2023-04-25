first_number = int(input())

sum_of_squares = first_number ** 2
sum_of_numbers = first_number

if first_number == 0:
    print(0)
else:
    while True:
        number = int(input())
        result = number ** 2

        sum_of_numbers += number
        sum_of_squares += result

        if sum_of_numbers == 0:
            print(sum_of_squares)
            break
