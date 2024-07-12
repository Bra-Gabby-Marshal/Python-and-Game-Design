# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = ['d', 'e', 'f']

# zipped = zip(list1, list2, list3)
# print(list(zipped))

# Unzip
zipped_list =[(1, 'a', 'd', 'g'), (2, 'b', 'e', 'h'), (3, 'c', 'f', 'i')]

unzipped = zip(*zipped_list)
list1, list2, list3, list4 = unzipped

# print(list(list1), (list2), (list3))
print(list(list1))
print(list(list2))
print(list(list3))
print(list(list4))