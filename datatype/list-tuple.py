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


#補充:
#list:
x=[1,2,3,4]
x.append(100)  #就是x+=[100],要注意是()
#print(x)  #[1,2,3,4,100]
x.insert(0,55)   #insert(位置,新元素):在指定位置插入新元素
print(x)  #[100,1,2,3,4](就是x[0]=100的意思)
x.remove(1) #移除元素(也可以x[0]=[])
x.pop(0)#從指定位置刪除元素
x.clear()#清空列表
#小技巧:複製list
x1=[1,2,4,6,7]
x2=x1[:]
x3=x1[::-1] #flip and copy
#list的排序:sort/sorted
x=[1,2,34.,6,9,100]
x.sort()  #(x2=sortde(x))
print(x)
x.sort(reverse=True)  #x2=sorted(x,reverse=True)
#用for快速生成列表
list1=[x for x in range(1,11)]  #產生一個1到10的列表
list2=[x+y for x in "abc" for y in "123"] #只能是字串的結合,會產出一個元素為xy結合的list

#list與tuple的互換
x=[1,2,3]
x2=tuple(x)
x3=list(x2)


