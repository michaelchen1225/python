import string
w=string.punctuation
l=int(input("how many lines?"))
tl=l
o=""
while tl>0:
    o+=input()
    tl-=1
o=o.upper()
for p in o:
    if p in w:
        o=o.replace(p,"")
o=o.split()
o="".join(o)
o=list(o)
o.sort()
c=0
for i in range(0,len(o)):
    try:
        f=int(o[i])
        c+=1
    except:
        continue
del o[0:c]   
o2={x:0 for x in o}
k=list(o2.keys())
count=0
for i in range(0,len(k)):
   count+=o.count(k[i])
   o2[k[i]]+=count
   print(k[i],"=",count)
   count=0

    


