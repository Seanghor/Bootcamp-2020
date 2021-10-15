# My code 34
def dict_search(info_students, str):
    x = []

    if str in info_students:
        x.append(info_students[str])
        for i in x:
            print(f'\"{i}\"')
    elif str not in info_students:
        print(f'"ERROR: {str} key not found"')

info_students = {
"username": "sabbe_k",
"score": 100,
"comments": "Good job!"
}
dict_search(info_students, "username")
print('=='*10)
dict_search(info_students, "score")
print('=='*10)
dict_search(info_students, "comments")
print('=='*10)
dict_search(info_students, "email")
print('=='*10)
dict_search(info_students, "phone_number")






# Use with return
def dict_search(info_students, str):

    if str in info_students:

        re = info_students[str]

    elif str not in info_students:
        re = f'ERROR: {str} key not found'

    return re

info_students = {
"username": "sabbe_k",
"score": 100,
"comments": "Good job!"
}

print(dict_search(info_students, "username"))
print('=='*10)
print(dict_search(info_students, "score"))
print('=='*10)
print(dict_search(info_students, "comments"))
print('=='*10)
print(dict_search(info_students, "email"))
print('=='*10)
print(dict_search(info_students, "phone_number"))
