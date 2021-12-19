#載入內建的模組sys並取得資訊
import sys    #import sys as system:取別名,所以---->print(system.platform)
print(sys.platform)    #印出系統資訊
print(sys.maxsize)     #印出最大值
print(sys.path)
#建立geometry模組並載入使用
import geometry
result=geometry.distance(1,1,5,5)
print(result)










