from random import randint
def getCode():
    bit1=randint(1,8)
    bit2=randint(1,8)
    bytelist=[]

    for i in range(1,9):
        if (i==bit1):
            bytelist.insert(bit1,'1')
        elif(i==bit2):
            bytelist.insert(bit2,'1')
        else:
            bytelist.insert(i,'0')
            
    code=""
    for i in range(1,9):
        code=code+bytelist.pop()
    print(code)

    i=len(code)-1
    sum=0
    for c in code:
        c=int(c)
        #print("char",c)
        sum=sum+(2**i)*c
        i=i-1
    print(sum)
    