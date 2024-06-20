'''
def sen(n):
    if(n==0):
        return 0
    return n+sen(n-2)
n=11
if(n%2==0):
    print(sen(n))
else:
    print(sen(n-1))
    '''
def l(n):
    if a[n]==None:
        if(n%2==0):
            print("yes")
    else:
        print("No")
    l(n+1)
a=[5,8,9,5,2,4,7]
l(0)