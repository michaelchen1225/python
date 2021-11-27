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
for x in range(1,11):   #for 變數名 in list或string  range(n):一種列表,表示0到n-1的數字 ramge(5,10)=[5,6,7,8,9]
    sum=sum+x  #分別放入1--10
print(sum)       