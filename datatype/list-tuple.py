#有序可動列表List 中括號
grades=[12,60,15,70,90] 
print(grades)
print(grades[0]) #索引取得跟字串一樣,也有編碼,先取得list再用[]取得索引
#grades[0]=55 #更新資料(把55放到列表中的第一個位置)
#print(grades[1:4]) #從1取到4 但不包含4
#grades[1:4]=[] #連續刪除列表中1到4(不包刮) 的資料
#grades=grades+[12,33] #再原本列表後做串接
#length=len(grades) #len(列表)可取得列表長度
#print(len(grades)) #就等於print(length)
#data=[[3,4,5],[6,7,8]] #巢狀列表
#print(data[0][1])#取得列表中第一個元素裡的編號1
#data[0][0:2]=[5,5,5,5]#代表第一個元素裡從編號0取到2(不包含),然後用[5,5,5,5]取代

#有序不可變動列表 touple 小括號
data=(3,4,5)
#操作跟list很像,但不能變動資料
data[0]=5 #erro