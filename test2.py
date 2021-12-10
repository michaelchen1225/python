def fac(s):
    if s==1:
        return 1
    else:
        return s*fac(s-1)
print(fac(4))

