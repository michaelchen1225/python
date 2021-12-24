#练习1：实现计算求最大公约数和最小公倍数的函数。
def gcd(x,y):
    if x>y:
        x,y=y,x
    else:
        g=0
        for i in range(1,x):
            if x%i==0 and y%i==0:
                g=i
    return g

def lcm(x,y):
    return x * y // gcd(x, y)


#练习2：实现判断一个数是不是回文数的函数
def is_palindrome(num):
    num=str(num)
    if num[0:len(num):1]==num[::-1]:
        return int(num)
#练习3：实现判断一个数是不是素数的函数
def is_prime(p):
    f=0
    for i in range(1,p+1):
        if p%i==0:
            f+=1
    if f<=2:
        return p
#练习4：写一个程序判断输入的正整数是不是回文素数
k=int(input("enter a number:"))
if is_palindrome(k)==is_prime(k):
    print("%d是回文質數" %k)

