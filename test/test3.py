import string
c=string.punctuation
print(c)
x=["1","2","3","A","B","c","!"]
for p in x:
    if p in c:
        x.remove(p)
print(x)