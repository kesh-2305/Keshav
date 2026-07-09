num = int(input("enter your whole number sir ji: "))

i = 1
print("factors of", num,"are: ")

while i <= num :
    if num % i == 0 :
        print(i)
    i = i + 1