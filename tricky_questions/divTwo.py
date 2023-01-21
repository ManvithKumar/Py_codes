def divide(num,denum):
    neg =0
    qnt = 0
    if num== 0 or denum ==0:
        return 0
    if num < 0 :
        num = -num 
        neg =1 
        if denum < 0:
            denum = -denum
            neg = 0
    if denum < 0:
        denum = -denum
        neg =1
        if num < 0:
            num = -num
            neg =0
    while num >= denum:
        num -=denum
        qnt+=1
    if neg ==1:
        qnt =-qnt
    return qnt

a = 100
b= 2
print(divide(a,b))
