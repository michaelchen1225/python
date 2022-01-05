#數字運算 
#root=4**0.5 #開根號(4的0.5次)
#print(root)
mod=7%3 #取餘數
print(mod)
#y=2+4
#print(y)
#y+=1 #y=y+1 將變數中的數字加1 y-=1就是把變  數中的數字減1 乘除以此類推
#print(y)
# s=3//2  取整數
#print(s) 印出1

#字串運算
s="hello"
print(s)
ss="hell\"o" #想在雙引號中表達雙引號:用反斜線關掉
s="hello"+"world"#串接(也可用空白)
s="hello\nworld"#斜線n換行
s="""hello
world""" #也是換行
print(s)
st="hello"*3+"world" #重複字串N次:*N
print(st)
s1="abcdef"
print("g" in s1) #用in或not in 判斷字串內容(結果為布林值)
#字串會對內部的字作編號(索引) 從0開始
ind="hello"
print(ind[0]) #取得第0個字元
print(ind[1:4])#從1取到4,但不包含4 (ell)
print(ind[1:])#從1取到最後
print(ind[:4])#從頭取到4 但不包含4
print(ind[:])#從頭取到尾
print(ind[::2])#從頭開始每隔2個取到尾
print(ind[1:4:2])#從第一個開始每隔2個取到4(不包含)
print(ind[-3])#取倒數地3個
print(ind[-3:])#取倒數前3個
print(ind[::-2])#從尾開始每隔兩個取道頭
print(ind[::-1])#印出頭尾相反的兩個字串
round(2.6)  #四捨五入   round(n1,n2)  n2:小數點第n2位

str1 = 'hello, world!'
# 计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1(找不到)
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
