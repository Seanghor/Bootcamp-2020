def odd_even_list(my_list):

    # convert item integer in list to string
    result = ['EVEN' if item%2 == 0 else 'ODD' for item in my_list]

    print(result)

odd_even_list([])
odd_even_list([1, 22, 111, 444])
odd_even_list([2, 11, 222, 333])
odd_even_list([1, 2, 3, 4, 555])




# Noted
# print('==='*20)
# my_list = [11, 22, 33, 23, 56]
# res = ['EVEN' if item%2 == 0 else 'ODD' for item in my_list]
# print(res)


# China
# def odd_even_list(list):
#     list1 = []
#     for i in list:
#         if i % 2 == 0:
#             list1.append('EVEN')
#         else:
#             list1.append('ODD')
#     return list1
#
# print(odd_even_list([]))
# print(odd_even_list([1, 22, 111, 444]))
# print(odd_even_list([2, 11, 222, 333]))
# print(odd_even_list([1, 2, 3, 4, 555]))
