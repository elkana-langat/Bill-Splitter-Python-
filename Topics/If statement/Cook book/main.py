pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

name_of_ingredient = input()

if name_of_ingredient in pasta:
    print("pasta time!")
if name_of_ingredient in apple_pie:
    print("apple pie time!")
if name_of_ingredient in ratatouille:
    print("ratatouille time!")
if name_of_ingredient in chocolate_cake:
    print("chocolate cake time!")
if name_of_ingredient in omelette:
    print("omelette time!")