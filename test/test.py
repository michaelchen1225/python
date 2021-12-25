def test(x):
    s=0
    for k in x:
        s+=k
    s/=len(x)
    print("平均數為%.1f" %s)
    m=0
    f=len(x)
    if len(x)%2==0:
        m=(x[f//2]+x[f//2-1])/2
        print("中位數為%.1f" %m)
    else:
        m=x[(f-1)//2]
        print("中位數為%.1f" %m)
test([1,2,3,4,5,6])
test([1,2,3,4,5])