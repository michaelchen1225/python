x=["1","2","3",'4','5','6',"7","8","9","10"]


if len(x)>9:
        for k in range(0,9):
            x[k]="s0"+x[k]
        for j in range(9,len(x)):
            x[j]="s"+x[j]
if len(x)<=9:
        for k in range(0,len(x)):
            x[k]="s0"+x[k]
print(x)



        