a = 23
b = 12
c = 294

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
print(greatest(a, b, c))