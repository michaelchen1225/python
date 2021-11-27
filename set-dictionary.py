#集合的運算  集合:一群資料 沒有順序的概念(用大括號)
#s1={3,4,5}
#print(10 in s1)  #判斷3是否在集合內 結果用True/False表示 也可以用not in 判斷資料是否在集合中
#s2={4,5,6,7}
#s3=s1&s2       #&交集:取兩個集合中相同的資料
#s4=s1|s2      #|聯集:取兩個集合中的所有資料,但不重複
#s5=s1-s2  #差集:從s1中減去與s2重複的部分
#s6=s1^s2  #反交集:取兩個集合中不同的部分
#s=set("hello")  #set(字串):自動將字串拆解成集合,但重複的部分不會在集合中重複出現
#print("A" in s) #set的應用:可拿來判斷一個字是否存在於字串中
#字典(鍵值對):也是用大括號->key-value的配對
dit={"apple":"蘋果","bug":"蟲"} #{"key":"value"}
#print(dit["apple"])   #取得value:用()取得字典載用[]取得key
#dit["apple"]="小蘋果" #修改value
#print(dit)  #取得整個字典
#print("apple" in dit) #用in/not in 判斷key是否在字典裡(不會判斷value!)
#del dit["apple"]  #刪除字典中的鍵值對(連value也一起刪)
#print(dit)
dic={x:x*2 for x in [3,4,5]}
print(dic)
