def int_list(list1):
    if list1 == []:
        re = 'False'


    elif list1 != []:
        for values in list1:


            # use if, else in loop to check each value in list1
            if type(values) == int:
                re = 'True'

            else:
                re = 'False'
                break

    return re



print(int_list([]))
print(int_list([1, 2, 3]))
print(int_list([1.5, 2, 2.0]))
print(int_list([100, 200, 300, 400, 500]) )
print(int_list(['100', '100', '200', '300']))
