#break的簡易範例
# n=0
# while n<5:
#     if n==3:
#         break  #跳出迴圈
#     print(n)   #印出迴圈中的n
#     n+=1
#print("最後的n: ",n)    #印出結束迴圈後的n
#continue的簡易範例
# n=0
# for x in [0,1,2,3]:
#     if x%2==0:   #x是否為整數
#         continue  #直接執行下一次的迴圈
#     print(x)
#     n+=1
# print("最後的n: ",n)
#else 的簡易範例
# sum=0
# for n in range(11):
#     sum+=n
# else:            #在迴圈結束前執行底下指令
#     print(sum)    #印出1加到10的結果


#綜合範例:找出整數平方根
#輸入9,得到3
#輸入11,得到沒有
n=input("輸入一個正整數: ")
n=int(n)   #轉換成數字
for i in range(n):     #i 從 0到n-1
    if i*i==n:
        print("整數平方根",i)
        break     #用break結束迴圈不會跑else
else:
    print("無整數平方根")
