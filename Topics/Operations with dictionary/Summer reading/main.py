import operator

# find the shortest book and print its title
# find the longest book and print its title

sorted_books = dict(sorted(books.items(), key=operator.itemgetter(1)))

page_count_list = list(sorted_books.values())

highest_page_count = page_count_list[0]
len_of_list = len(page_count_list)
lowest_page_Count = page_count_list[len_of_list - 1]

for obj in sorted_books.items():
    if obj[1] == highest_page_count:
        print(obj[0])

for obj in sorted_books.items():
    if obj[1] == lowest_page_Count:
        print(obj[0])