f = open("poem.txt")
content = f.read()
if("permar" in content):
    print("the word permar is persent in this content")

else:
    print("the word permar is not persent in this content")
f.close()