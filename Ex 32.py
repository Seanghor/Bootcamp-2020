# def dict_info(*dc):
#
#     my_list = ['firstname', 'lastname', 'email', 'phone']
#     dc[0] = dc[0][0].upper()
#     dc[1] = dc[1].upper()
#     print(dict(zip(my_list, dc)))
#
# dict_info('kelvin', 'sabbe', 'sabbe.kev@gmail.com', '+855 967827020')
# dict_info('', '', '', '')



# my_list = ['firstname', 'lastname', 'email', 'phone']
# my_list[0] = my_list[0].upper()
# print(my_list)


# def dict_info(firstname,lastname, email, phone):
#     data_list = ["firstname", "lastname", "email", "phone"]
#     new_firstname = firstname[0].upper() + firstname[1:]
#     new_lastname = lastname.upper()
#     new_dc = dict(zip(data_list, [new_firstname, new_lastname, email, phone]))
#     return new_dc
#
# print(dict_info('kelvin', 'sabbe', 'sabbe.kev@gmail.com', '+855 967827020'))


# Kimsour
def dict_info(firstname,lastname, email, phone):
    my_list = ['firstname', 'lastname', 'email', 'phone']
    if email == "" or phone == "" or firstname != "" or lastname != "" :
        f_name = firstname[0].upper() + firstname[1:]
        l_name = lastname.upper()
        value = [f_name, l_name, email, phone]
        mix = zip(my_list, value)
        return dict(mix)

        # if firstname == "" or lastname == "":
        #     return dict(zip(my_list, [firstname, lastname, email, phone]))
        # else:
        #     f_name = firstname[0].upper() + firstname[1:]
        #     l_name = lastname.upper()
        #     value = [f_name, l_name, email, phone]
        #     mix = zip(my_list, value)
        #     return dict(mix)
    # elif firstname == "" or lastname == "":
    #     # if firstname == "" or lastname == "":
    #     #     return dict(zip(my_list, [firstname, lastname, email, phone]))
    #     # else:
    #     f_name = firstname[0].upper() + firstname[1:]
    #     l_name = lastname.upper()
    #     value = [f_name, l_name, email, phone]
    #     mix = zip(my_list, value)
    #     return dict(mix)
    else:
        f_name = firstname[0].upper() + firstname[1:]
        l_name = lastname.upper()
        value = [f_name, l_name, email, phone]
        mix = zip(my_list, value)
        return dict(mix)

print(dict_info("kevin", "sabbe", "sabbe.kev@gmail.com", "+855 16 804 404"))
print(dict_info("", "", "", ""))
print(dict_info("kevin", "sabbe","",""))
print(dict_info("", "", "sabbe.kev@gmail.com", "+855 16 804 404"))
