# My Code
def find_all(myList, value):
    last = []
    for i in range(0, len(myList)):
        if myList[i] == value:
            last.append(i)
            re = last
        # can not use: elif != value:

    if value not in myList:
        re = 'None'

    elif myList == []:
        re = 'None'


    return re

print(find_all([], 1))
print(find_all(['Hello'], 'Bye'))
print(find_all(['A', 'B', 'C', 'C', 'B', 'C', 'C'], 'C'))
print(find_all([1, 5, 12, 5, 4], 5))




# Beta but Error some condiction
# def find_all(myList, l):
#     last = []
#     if len(myList) > 0:
#         for i in range(0, len(myList)):
#             value = myList[i]
#
#             if value == l:
#                 last.append(i)
#                 fb = last
#
#             elif value != l:
#                 fb = 'None'
#
#
#
#     elif len(myList) == 0:
#         fb = 'None'
#
#     print(fb)
#
# find_all([], 1)
# find_all(['Hello'], 'Bye')
# find_all(['A', 'B', 'C', 'C', 'B', 'C', 'C'], 'C')
# find_all([1, 5, 12, 5, 4], 5)



