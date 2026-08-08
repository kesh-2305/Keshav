def sum_numbers(*args):
    print(type(args))
    print(args)

    sum = 0
    for num in args:
        sum += num
    return sum    

print(sum_numbers(1,2,3,4,5))