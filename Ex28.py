# My Code
def list_number(start, end, reversed=''):
    my_list = []

    for i in range(start, end+1):
        my_list.append(i)

    if reversed == True:
        result = sorted(my_list, reverse = True)
        print(result)
    else:
        print(my_list)


list_number(1, 10)
list_number(1, 10, reversed=True)
list_number(1, 10, reversed = False)
list_number(20, 25)
list_number(20, 25, reversed=True)


print('=='*20)
# China
def lisst_number(num1, num2, reversed=''):
    list = []
    for i in range (num1, num2+1):
        list.append(i)
    if reversed==True:
        list1 = sorted(list, reverse=True)
        list = list1
    else:
        pass
    return list

print(lisst_number(1, 10, reversed=False))
print(lisst_number(1, 10, reversed=True))
print(lisst_number(1, 10))
