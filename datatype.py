#number
3456
3.14
#字串
"中文"
"Hello"
#布林值
True
False
#list有順序可動的列表
[3,4,5,6]
["hello","world"]
#有順序不動的列表Tuple
(3,4,5)
("hello","my python")
#集合
{3,44,5,}
#字典Dictionary
{"apple":"蘋果","data":"資料"}
#變數:用來儲存資料的自訂名稱(用英文,頭不能是數字)
X=3
#print(資料)
print(3)
x=True #replaced 3 with True

# type 偵測型態
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>
print(type(d))    # <class 'str'>
print(type(e))    # <class 'bool'>
print("-----------")


#可用在判斷中
x=5
if type(x)==str :
    print(x)
else:
    print("fail")
#補充:變數互換
a=1
b=2
a,b=b,a
print(a,b)