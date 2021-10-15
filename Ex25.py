# My code
def sort_set(list1):
    set1 = set(list1)    # set to Set to get item without duplicate
    new1 = list(set1)
    result1 = sorted(new1, reverse = False)
    print(result1)

def sort_set_rev(list2):
    set2 = set(list2)
    new2 = list(set2)
    result2 = sorted(new2, reverse = True)
    print(result2)

sort_set([])
sort_set(['Hello'])
sort_set(['A', 'B', 'C', 'C', 'B'])
sort_set([1, 5, 12, 5, 4])


print('=='*20)

sort_set_rev(['A', 'B', 'C', 'D', 'E'])
sort_set_rev(['100', '100', '200', '300'])
sort_set_rev([1, 5, 12, 5, 4])

print('=='*20)
l = ['seanghor']
for i in l:
    print(i)   # ==> Seanghor


# China
# def fun_split(list1):
#     set1 = set(list1)
#     list2 = list(set1)
#     ascending_order = sorted(list2)
#     return ascending_order
# print(fun_split([1, 5, 12, 5, 4]))
#
# def fun_split_rev(list1):
#     set1 = set(list1)
#     list2 = list(set1)
#     decending_order = sorted(list2, reverse=True)
#     return decending_order
# print(fun_split_rev([1, 5, 12, 5, 4]))

# list = [1, 5, 12, 5, 4, 5, 4]
# table = []
# for i in list:
#     if i not in table:
#         table.append(i)
# print(table)
