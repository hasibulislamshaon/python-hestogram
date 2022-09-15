dic=dict()
line=input("Enter the text line: ")
words=line.split()
print(words)
for word in words:
    dic[word]=dic.get(word,0)+1
print(dic)

