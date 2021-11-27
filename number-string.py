#數字運算
#root=4**0.5 #開根號(4的0.5次)
#print(root)
mod=7%3 #取餘數
print(mod)
#y=2+4
#print(y)
#y+=1 #y=y+1 將變數中的數字加1 y-=1就是把變  數中的數字減1 乘除以此類推
#print(y)
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
round(2.6)

