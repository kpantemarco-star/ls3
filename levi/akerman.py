def ackerman(a,b):
    if a == 0 : 
        print(b+1) 
 
    elif b == 0 :
         print(ackerman((a-1),1)) 
    # else :
    #    print(ackerman((a-1),ackerman(a,(b))))

ackerman(5,0)