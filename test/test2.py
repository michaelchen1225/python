N=int(input("顧客數目:"))
T=int(input("交易數目:"))
t=T
Tt=T
o=""
m=[]
p=[]
total=0
while T>0:
    o+=input()
    m.append(int(o[0]))
    m.append(int(o[2]))
    m.append(int(o[4:len(o)]))
    o=""
    T-=1
C={x:x*0 for x in range(0,N)}
while t>0:
    p=m[0:3]
    if p[1]==1:
        C[p[0]]+=p[2]
    elif p[1]==2:
        C[p[0]]-=p[2]
    elif p[1]==3:
        a={p[0]:p[2]}
        C.update(a)
    elif p[1]==4 and C[p[0]]==0:
        del C[p[0]]
    del m[0:3]
    p=[]
    t-=1
for k in range(0,Tt+1):
    try:
        total+=C[k]
    except:
        continue
print(C)
print("存款總和:",total)

