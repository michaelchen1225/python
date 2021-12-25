def describe(L):
    s=0
    L.sort()
    for k in L:
        s+=k
    s/=len(L)
    m=0
    f=len(L)
    if len(L)%2==0:
        m=(L[f//2]+L[f//2-1])/2
    else:
        m=L[(f-1)//2]
    return s,m

L=[30, 20, 10, 30, 30, 40]
(mea, med)= describe(L)
print("平均數: ", mea)
print("中位數: ", med)
  
        