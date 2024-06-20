def dc(temp1):
    temp2=temp1
    while temp1>9:
        sum1=0
        while temp1>0:           
            rem=temp1%10
            sum1=sum1+rem
            temp1=temp1//10            
        temp1=sum1        
    prime(temp1,temp2)
def prime(temp1,temp2):
    if(temp1 in [2,3,5,7]):
        print(temp2)
    else:
        temp2=temp2+1
        dc(temp2)
n=int(input("Enter number:"))
temp1=n
dc(temp1)
#m=sum(list(map(int,n))),return statement will always sent to previous function call
"""
def fuc(x):
    if(x==3):
        return 500
    print(x)
    t=fun(x+1)
    print(x)
    return t
print(fun(1))
o/p:
1 2 2 1 500

def fun(x,s):
    if(x==len(a)):
        return s
    s=s+a[x]
    return fun(x+1,s)
a=[6,7,8]
print(fun(0,0))
o/p:21
"""
