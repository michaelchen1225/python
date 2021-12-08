#Problem 1. 階乘函式應用¶
#N!為N的階乘等於N*(N-1)*(N-2)* ‧‧‧*3*2*1
print("輸入一個整數N，求S(N)=1 - 2**2/2! + 3**2/3! - 4**2/4!‧‧‧N**2/N!=？")
def fac(s):
    if s==1:
        return 1
    else:
        return s*fac(s-1)
x=int(input("enter a number:"))
f=1
sum=0
for y in range(1,x+1):
    sum+=((y**2)/fac(y))*f
    f*=-1
print(sum)

print("---------------")

print("Problem 2. 計算並印出A和B之間的質數")
def is_prime(i):
    f=0
    for x in range(1,i+1):
        if i%x==0:
            f+=1
    if f<=2:
        return "isp"
    else:
        return "nop"
    
A=int(input("enter a number:"))
B=int(input("enter a number:"))
count=0
if A>B:
    A,B=B,A
for y in range(A,B+1):
    if is_prime(y)=="isp":
        print(y)
        count+=1
print("質數的數量是：%d" %count)

print('-----------------')

print("Problem 3. 閏年函式應用")
def is_leap_year(N):
    if N%4==0 and N%100!=0:
        return True
    elif N%400==0:
        return True
    else:
        return False
N1=int(input("enter a AD year:"))
N2=int(input("enter a AD year:"))
count=0
if N1>N2:
    N1,N2=N2,N1
for x in range(N1,N2):
    if is_leap_year(x)==True:
        count+=1
print(count)




