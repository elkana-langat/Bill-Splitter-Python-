number_of_halls = int(input())
capacity = int(input())
number_of_viewers = int(input())

can_hold = number_of_halls * capacity >= number_of_viewers
if can_hold:
    print(True)
else:
    print(False)
