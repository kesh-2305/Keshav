def function_all (a, b, *args, **kwargs):
    print(a)
    print(b)
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    
    sum =0
    for num in args:
        sum += num
    return sum

print(function_all(5,6,12,3,4,7,6,name= "Keshav", age= 99, city= "Bhiwani"))

