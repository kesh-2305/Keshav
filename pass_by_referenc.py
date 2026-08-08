my_list = (1,2,3)

def modify_list(li):
    li.append(5)
    print(li)

print("befor calling the func", my_list)

modify_list(my_list)

print("after calling the func", my_list )