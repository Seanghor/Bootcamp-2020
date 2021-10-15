# My code 36
def dict_count(myList):
    str_value = []
    count_duplicate = []
    mySet = set(myList)
    for value in mySet:
        st = str(value)
        str_value.append(st)
    sort_str_value = sorted(str_value)     # string item

# convert integer item to string item in myList to count duplicate item
    new_str_list = [str(x) for x in myList]      # ['1', '1', '1', '1', '2', '2', '2', '3', '3', '4', '4', '5']

    for id in range(0, len(str_value)):                   # len(s) = 5 ==> id = 0, 1, 2, 3, 4
        count = new_str_list.count(sort_str_value[id])   # id = 0, 1, 2, 3, 4    and   s = [1, 2, 3, 4, 5]
        count_duplicate.append(count)


    mix = zip(sort_str_value, count_duplicate)
    dc = dict(mix)
    print(dc)

dict_count([1,1,1,1,2,2,2,3,3,4,4,5])
dict_count(["hey", "hi", "hi", "hi"])
dict_count(["python", "python", "c++"])
dict_count(["a", "b", "c", "d", "e"])
dict_count([])
