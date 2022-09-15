#Reviewing the previous day hestograms
multi=dict()
enter=input("enter the line: ")
words=enter.split()
for word in words:
    multi[word]=multi.get(word,0)+1
print(multi)