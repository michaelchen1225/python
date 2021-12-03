#练习1：英制单位英寸与公制单位厘米互换
l=float(input("輸入長度: "))
u=input("輸入單位: ")
if u == "cm":
    print("%.2fcm=%.2fin" %(l,l/2.54))
elif u == "in":
    print("%.2fin=%.2fcm" %(l,l*2.54))
else:
    print("請輸入有效單位")


#练习2：百分制成绩转换为等级制成绩
#要求：如果输入的成绩在:
#      90分以上（含90分）输出A
#      80分-90分（不含90分）输出B
#      70分-80分（不含80分）输出C
#      60分-70分（不含70分）输出D
#      60分以下输出E。
g=int(input("score:"))

if g >= 90:
    print("A")  #更:g="A",最後再print(g)就好
elif 80<=g<90:  #底下類推
    print("B")
elif 70<=g<80:
    print("C")
elif 60<=g<70:
    print("D")
elif g<60:
    print("E")
#簡單的寫法:把print拿出if外面,這樣可以少打很多print

