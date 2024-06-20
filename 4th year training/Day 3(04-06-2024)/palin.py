'''
def palin(n1,rev):  
    if n1>0:
        rev=rev*10+(n1%10)
        return palin(n1//10,rev)
    return rev   
n=int(input())
n1=n
if(n==palin(n1,0)):
    print("palindrome")
else:
    print("Not a palindrome")
'''
'''
l=list(map(int,input().split()))
maxi=0
n=len(l)
for i in range(n-1):
    p=0
    for j in range(i+1,n):
        if(l[j]>l[i]):
            p=l[j]-l[i]
            if(p>maxi):
                maxi=p
print(maxi)

#method 2
l=list(map(int,input().split()))
bp=0
pr=0
for i in range(len(l)-1):
    if l[i+1]<l[i]:
        bp=l[i+1]
    else:
        for i in range(i+1,len(l)-1):
            if((l[i+1]-l[i])>pr):
                pr=l[i+1]-bp
print(pr)

'''

    


