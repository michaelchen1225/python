#載入內建的sys模組並取得資訊
import sys 
print(sys.platform)
print(sys.maxsize)   
import sys as s       #取別名
print(s.platform)     #同print(sys.platform)
print("--------")

#建立geometry模組,載入使用
import geometry    #import模組名稱                                                                       
result=geometry.dis(1,1,5,5)        #使用:模組名稱.模模組內函式
print(result)

