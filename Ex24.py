# My code
def fun_sort(myList1):
    result1 = sorted(myList1, reverse = False)
    print(result1)
fun_sort([])
fun_sort(['Hello'])
fun_sort(['A', 'B', 'C', 'D', 'E'])
fun_sort([1, 5, 12, 5, 4])

print('=='*20)
def fun_sort_rev(myList2):
    result2 = sorted(myList2, reverse = True)
    print(result2)
fun_sort_rev(['A', 'B', 'C', 'D', 'E'])
fun_sort_rev(['300', '100', '200', '400'])
fun_sort_rev([1, 5, 12, 5, 4])
