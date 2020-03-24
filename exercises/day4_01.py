
# referencyjność list

# list = [1, 2, 3]
# new_list = list
# print(list)
# list[0] = 'jeden'
# print(new_list)
# print(list)
#
# list = ['A', 'B', 'C']
# true_copy = list.copy()
# print(list)
# list[0] = '1'
# print(true_copy)
# print(list)


list_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(list_1)
import copy
new_list = copy.deepcopy(list_1)
print(list_1[1][1])
list_1[1][1] = 'X'
print(list_1[1][1])
print(new_list[1][1])