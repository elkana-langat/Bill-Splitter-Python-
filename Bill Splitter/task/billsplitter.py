import random

print("Enter the number of friends joining (including you):")
number_of_friends = int(input())

if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    names_of_friends = []

    print("Enter the name of every friend (including you, each on a new line:")
    for i in range(number_of_friends):
        names_of_friends.append(input())

    names_dict = dict.fromkeys(names_of_friends, 0)

    print("Enter the total bill value:")
    final_bill = int(input())

    # Each friends bill
    single_bill = round((final_bill / number_of_friends), 2)

    for key in names_dict:
        names_dict[key] = single_bill

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()  # if the user wants to use the feature

    if answer == "Yes":
        single_bill = (final_bill / (number_of_friends - 1))
        single_bill = round(single_bill, 2)
        lucky_user = random.choice(names_of_friends)

        names_dict = {values: single_bill for values in names_of_friends}
        names_dict[lucky_user] = 0

        print(f"{lucky_user} is the lucky one!")
        print()
        print(names_dict)
    else:
        print("No one is going to be lucky")
        print()
        print(names_dict)
