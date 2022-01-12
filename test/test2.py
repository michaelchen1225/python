k=o2.keys()
count=0
for i in range(0,len(k)):
   count+=o.count(k[i])
   o2[k[i]]+=count
   print(k[i],"=",count)
   count=0