print("Problem1:輸入一個整數N，求S(N)=1 - 2**2/2! + 3**2/3! - 4**2/4!‧‧‧N**2/N!=？")

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
print("質數的數量是:%d" %count)

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

print("------------")

print("Problem4:試撰寫一程式，輸入一整數N，找出N以內的所有完美數及其真因數。")

def is_perfect(N):
    f=0
    for x in range(1,N):
        if N%x==0:
            f+=x
    if f==N:
        return "isp"
def factor(F):
    q=""
    for x in range(1,F):
        if F%x==0:
            q+=str(x)
            q+="+"
    print(str(F),"=",q[0:len(q)-1])
n=int(input("enter a number:"))
count=0
for p in range(1,n+1):
    if is_perfect(p)=="isp":
        factor(p)
        count+=1
print(count)

print("------------------")

print("Problem5:Write an iterative function  that calculates the exponential baseexp ")

def iterPower(base, exp):
    f=exp-1
    n=base
    if exp==0:
        return 1
    else:
        while f>0:
            base*=n
            f-=1
    return base
print(iterPower(2,10))  #testing

print("----------------------")

print("Problem 6. power recur")

def recurPower(base, exp):
    if exp==0:
        return 1
    else:
        return base*recurPower(base,exp-1)
print(recurPower(2,6)) #test

print("Problem7:find GCD(itr&recur)")

def gcdIter(a, b):
    for x in range(1,b+1):
        if a%x==0 and b%x==0:
            xs=x
    return xs
print(gcdIter(12921,4234))

def gcdRecur(a, b):
    if b==0:
        return a
    else:
        return gcdRecur(b,a%b)
print(gcdRecur(42934,4234))





