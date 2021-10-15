
def dict_users(list):
    character = []            # to store Unsername and ID
    num = 0
    value = []
    re = []
    name = 'username'
    id = 'ID'
    for i in list:
        character.append(name)
        character.append(id)

        num += 1

        value.append(i)
        value.append(num)

        mix = zip(character, value)
        last = dict(mix)
        re.append(last)

    print(re)

dict_users(["Akai", "Roger", "Fanny", "Diggie"])
dict_users([])




# China
def dict_users(list):
    list1 = []
    id=1
    for i in list:
        dict = {'username': i,'ID': id }
        id+=1
        list1.append(dict)
    return list1
print(dict_users(["Akai", "Roger", "Fanny", "Diggie"]))

