#while 迴圈
#1+2+...10
#n=1
#sum=0 #紀錄累加的結果
#while n<=10:   #只要是true就會一直執行
 #   sum=sum+n
 #   n+=1
#print(sum)   #無縮牌就不再回圈內
#for loop
#1+2+...10
sum=0
for x in range(1,11):   #for 變數名 in list或string  
    sum=sum+x  #分別放入1--10
print(sum)   
print("lll")



#range
#range(101)：可以产生0到100范围的整数，需要注意的是取不到101。
#range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
#range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
#range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

#補充:使用時機
#  明确的知道循环执行的次数,推荐使用for-in循环
#  构造不知道具体循环次数的循环结构，推荐使用while循环。


#try/except
#如果要避免程式因錯誤而停止，
#可使用 try 和 except 進行保護 ( 或測試 )，
#當 try 區段內的程式發生錯誤時，
#就會執行 except 裡的內容，
#如果 try 的程式沒有錯誤，就不會執行 except 的內容
a = input('輸入數字：')
print(a + 1)       # 發生錯誤
print('hello')      # 因為發生錯誤，造成程式停止，所以後方程式無法執行

#try!
try:                      # 使用 try，測試內容是否正確
  a = input('輸入數字：')
  print(a + 1)
except:                   # 如果 try 的內容發生錯誤，就執行 except 裡的內容
  print('發生錯誤')
print('hello')