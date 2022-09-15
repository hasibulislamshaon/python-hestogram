dictionary=dict()
multiLine=input("Enter the line of words: ")
words2=multiLine.split()
for everyWord in words2:
    dictionary[everyWord]=dictionary.get(everyWord,0)+1
print(f"{dictionary}")
print(f"{dictionary.keys()}\n{dictionary.values()}\n{dictionary.items()}")
for keys,values in dictionary.items():
    print(keys)
    print(values)
bigcount=None
bigword=None
for word,dictionary in dictionary.items():
    if bigcount is None or bigcount<dictionary:
        bigword=word
        bigcount=dictionary
print(f"\n\n\n\n\n{bigword}  {bigcount}")
