

##def fib(x,x1=0,x2=1,c=0):
##    if(x<=0):
##        print('enter a valid number:')
##    elif(x==1):
##        print('fibanacci series:',x)
##    else:
##        
##        print('fibanacci series')
##        while(c<x):
##            print(x1,end=' ')
##            s=x1+x2
##            x1=x2
##            x2=s
##            c+=1
##           
##x=int(input('enter the term:'))
##fib(x)
x=int(input('enter the term:'))
x1=0
x2=1
c=0
if(x<=0):
    print('enter a valid number:')
elif(x==1):
    print('fibanacci series:',x1)
else:
    print('fibanacci series')
    for i in range(x1,x):
        print(x1)
        s=x1+x2
        x1=x2
        x2=s
