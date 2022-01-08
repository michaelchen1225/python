#集合的運算  集合:一群資料 沒有順序的概念(用大括號)
s1={3,4,5}
print(10 in s1)  #判斷3是否在集合內 結果用True/False表示 也可以用not in 判斷資料是否在集合中
s2={4,5,6,7}
s=set("hello")  #set(字串):自動將字串拆解成集合,但重複的部分不會在集合中重複出現
print("A" in s) #set的應用:可拿來判斷一個字是否存在於字串中
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}#快速生成set
print(set4)   #{3,5}

#set()用法
#建立空集合要使用 set()，使用 s = {} 是會建立空 dict
set1=set((1,2,3))   #帶入 tuple
set1=set(range(1,10))  #使用range

#add
set1.add(4)  #添加元素

#update
set1.update([1,3])   #set_name.update(list/tuple/set/dic)  合併其他的資料

#discard  (return:None)
set1.discard(1)   #刪除元素

#remove
set1.remove(3)    #刪除元素,當無此元素時會報錯

#運算
#交集&:取相同部分
fruits1 = {'apple','banana','orange','lemon'}
fruits2 = {'tomato','apple','banana'}
print(fruits1 & fruits2)   
#聯集|:取兩set的全部元素
print(fruits1 | fruits2)
#差集(set1-se2)
print(fruits1-fruits2)
#反差集(set1^set2):取出非焦急的元素

#注意:set無index的概念
#注意:set中無重複的資料

#字典(鍵值對):也是用大括號->key-value的配對
#創建字典
items1 = dict(one=1, two=2, three=3, four=4)  #1
dit={"apple":"蘋果","bug":"蟲"} #{"key":"value"}  #2
items3 = {num: num ** 2 for num in range(1, 10)}  #3

print(dit["apple"])   #取得value:用()取得字典載用[]取得key
#修改
dit.update(a=5)  #注意:用小括號  dit1.update(dit2)
dit["apple"]="小蘋果"
dit.pop("a")

print(dit)  #取得整個字典
print("apple" in dit) #用in/not in 判斷key是否在字典裡(不會判斷value!)
del dit["apple"]  #刪除字典中的鍵值對(連value也一起刪)

#keys()列出字典所有的鑑
x=dict(a=1,b=3,c=5)
print(list(x.keys()))
#以列表形式印出

#values() 列出所有值

