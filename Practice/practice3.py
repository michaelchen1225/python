#练习1：输入一个正整数判断是不是質数
i=int(input("輸入一個正整數:"))
f=0
for x in range(1,i+1):
    if i%x==0:
        f+=1
if f<=2:
    print("%d是質數" %i)
else:
    print("%d不是質數" %i)

#练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。    
x=int(input("input a number:"))
y=int(input("input a number:"))
for a in range(1,x+1):
    if x%a==0 and y%a==0:
        xs=a
print(xs)

gh=1
while (x*gh)%y!=0:
    gh+=1
else:
    print(x*gh)