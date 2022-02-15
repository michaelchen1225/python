N=int(input("顧客數目:"))
T=int(input("交易數目:"))
t=T
o=""
m=[]
p=[]
total=0
while T>0:
    o+=input()
    m.append((o[0:3]))
    m.append((o[4]))
    m.append((o[6:len(o)]))
    o=""
    T-=1
C={x:x*0 for x in range(1,N+1)}
cus=list(C.keys())
amo=list(C.values())
if len(cus)>9:
        for k in range(0,9):
            cus[k]="s0"+str(cus[k])
        for j in range(9,len(cus)):
            cus[j]="s"+str(cus[j])
if len(cus)<=9:
        for k in range(0,len(cus)):
            cus[k]="s0"+str(cus[k])
C=dict(zip(cus,amo))
while t>0:
    p=m[0:3]
    if p[1]=="1":
        print(C[p[0]])
        print(int(p[2]))
        C[p[0]]+=int(p[2])
    elif p[1]=="2":
        C[p[0]]-=int(p[2])
    elif p[1]=="3":
        a={p[0]:int(p[2])}
        C.update(a)
    elif p[1]=="4" and C[p[0]]==0:
        del C[p[0]]
    del m[0:3]
    p=[]
    t-=1
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
a=list(C.values())
(me, va, ra, ms)= describe(a)
print("平均數:", me)
print("變異數:", va)
print("範圍：", ra)
print("中位數：", ms)
