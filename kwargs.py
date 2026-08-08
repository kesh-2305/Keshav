def display_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, "=", value)

display_info(name = "Keshav", age = 99, city = "Bhiwani", vill = "Phoolpura" )