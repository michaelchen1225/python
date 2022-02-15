
def describe(L):
    """
    """
    s=0
    for x in range(0,len(L)):
        s+=L[x]
    mean=s/len(L)
    s=0
    for x in range(0,len(L)):
        s+=(L[x]-mean)**2
    var=s/(len(L)-1)
    L.sort()
    ran=L[len(L)-1]-L[0]
    m=0
    f=len(L)
    if len(L)%2==0:
        m=(L[f//2]+L[f//2-1])/2
    else:
        m=L[(f-1)//2]
    return (mean, var, ran, m) 