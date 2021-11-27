#定義函式
#函式內部程式碼,若沒有進行函式呼叫就不會執行
def multiply(x,y):
    print(x*y)
    return  x*y   #函式結束後如果沒有定義return,回傳None
#呼叫函式
value=multiply(3,5)
print(value)  #因為函數有回傳值,所以會印出12和None

#例1:
def multiply(x,y):
    return(x*y)
value=multiply(3,4)+multiply(6,5)
print(value)
#函式的包裝  同樣的邏輯可重複利用
def calculate(max):      #1加到max
    sum=0
    for x in range(1,max+1):
        sum+=x
    print(sum)
calculate(21)
