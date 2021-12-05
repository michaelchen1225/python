#參數的預設資料
def power(base,exp=0):    #預設exp=0,當呼叫function時可以不餵資料給exp
    print(base**exp)
power(3)        #印出1(沒給定資料,exp預設為0)  !!!:若沒給exp預設值,又沒給定資料給exp,會error
power(3,2)      #印出9(有給定2給exp)
print("-----------------------")
#使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(2,4)   #印出0.5 (無對應參數時,第一個給n1,第二個給n2)
divide(n2=8,n1=16)   #印出2(有對應參數)
print("------------------------")
#不定參數數量
def test(*ts):  #加*
    print(ts)    #以touple型式印出(1,4,7,3),(1,4,8)   

test(1,4,7,3)     
test(1,4,8)    

#算平均
def avg(*ns):
    sum=0
    for x in ns:
        sum+=x
    print(sum/len(ns))
avg(1,2,3,4)
avg(45,55)
print("-------------------------")
#算組合數(c)
def fac(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result     
m = int(input('m = '))
n = int(input('n = '))
# 当需要计算阶乘的时候不用再写循环求阶乘而是直接调用已经定义好的函数
print(fac(m) // fac(n) // fac(m - n))

