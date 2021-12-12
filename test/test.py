def gcdIter(a, b):
    for x in range(1,b+1):
        if a%x==0 and b%x==0:
            xs=x
    return xs
print(gcdIter(12921,4234))