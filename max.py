a = int(input( ))
b = int(input( ))
c = int(input( ))
numbers = (a, b , c)
def find_largest(numbers):
    if (numbers[0] > numbers[1] and numbers[0] > numbers[2]):
        print("a is largest", numbers[0])
    elif(numbers[1]>numbers[0] and numbers[1]>numbers[2] ):
        print("b is largest", numbers[1])
    else:
        print("c is largest", c)
find_largest(numbers)