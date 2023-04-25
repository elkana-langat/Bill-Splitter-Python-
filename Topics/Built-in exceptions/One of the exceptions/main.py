index_of_exception = int(input())

exception_list = dir(locals()['__builtins__'])

print(exception_list[index_of_exception])