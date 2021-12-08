def is_prime(i):
    
    # Your code here
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