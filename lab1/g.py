def toDecimal (bi,i,j):
    if i<0 :
        return 0
    else :    
        return int(bi[j])*(2**i)+toDecimal(bi,i-1,j+1)
bit=input()
l=len(bit)
print(toDecimal(bit,l-1,0))


