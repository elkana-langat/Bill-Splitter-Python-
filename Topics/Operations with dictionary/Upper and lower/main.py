# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
new_dict = {values.upper(): values.lower() for values in some_iterable}

print(new_dict)
