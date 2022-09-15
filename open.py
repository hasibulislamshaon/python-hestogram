n=input("file name : ")
x=open(n)
for line in x:
    word=line.split()
print(word)
    