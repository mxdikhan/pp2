def toDecimal (bi,i,j):
    if j<0 :
        return 0
    else :    
        return int(bi[j])*(2**i)+toDecimal(bi,i+1,j-1) 
bit=input()
l=len(bit)
print(toDecimal(bit,0,l-1))



