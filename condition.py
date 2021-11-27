#判斷式
#x=input("請輸入數字: ")  #取得字串型式的使用者輸入 注意是字串型式!  (然後X就被指定給輸入的東西)
#x=int(x)   #將字串型態改成整數的數字型態(這樣才能比較大小)
#if x>200:   #回傳布林值True/False    注意1:要記得加冒號! 注意2:if,elif,else只會跑其中一行-->跑完跳出,所以要一次看整個結構
#   print("大於200")      #只有在回傳True下才會執行,若false,再看底下判斷式
#elif x>100:                #若回傳False就會到這一行進行判斷,若true,執行指令,若false,看else 
#    print("大於100. 小於等於200") 
#else:                      #在上面回傳False才會被執行   
#    print("小於100")      
#四則運算
n1=int(input("請輸入數字一: "))  #先輸入數字一
n2=int(input("請輸入數字二: "))  #再輸入數字二
op=input("請輸入運算: +,-,*,/: ")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print("n1/n2")
else:
    print("不支援的運算")