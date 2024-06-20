'''def combination(l,k):
    def fun(curr,start):
        if(len(curr)==k):
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=[3,5,1,6,7]
k=3
combination(a,k)
'''
#fibonnacci series
'''
def fun(x):
    if x==1:
        return 1
    if x==2:
        return 1
    return fun(x-1)+fun(x-2)
n=10
for i in range(1,n+1):
    print(fun(i),end=" ")
'''
'''
ip:school
3
l 2-hoolsc
r 3-oolsch
l 1-chools
'''
'''   
s="school"
n=3
d=['l','r','l']
v=[2,3,1]
l=len(s)
ans=''
for i in range(0,n):
    if(d[i]=='l'):

        ans=ans+s[v[i]]
    elif(d[i]=='r'):
        ans=ans+s[l-v[i]]

l1=[]
i=0
k=0
a1=''
a1=sorted(ans)
while(i<l-n+1):
    s1=""
    for j in range(n):
        s1=s1+s[k]
        k=k+1
    k=i+1
    l1.append(s1)
    i=i+1
print(l1)
a1=''.join(sorted(ans))
print(a1)
print(sorted(ans))
l2=[]
for i in range(len(l1)):
    l2.append(sorted(l1[i]))
if(sorted(ans) in (sorted(l2))):
    print("yes")
else:
    print("No")
'''   
'''
#method2-optimized one
s=input()
n=int(input())
str=[]
for i in range(n):
    b=input()
    if b[0]=='L':
        str.append(s[int(b[2])])
    else:
        str.append(s[-int(b[2])])
str.sort()
arr=[]
for i in range(len(s)-n+1):
    t=list(s[i:n+i])
    t.sort()
    arr.append(t)
#print(arr)
if str in arr:
    print("yes")
else:
    print("no")
'''
#index and number-1 prime or not i++,num--, till half of the num
def isprime(x):
    if(x==1):
        return 1
    if(x==2):
        return 1
    for i in range(2,(x//2)+1):
        if(x%i==0):
            return 0
    return 1

a=int(input())
for i in range(1,(a//2)+1):
    if(isprime(i) and isprime(a-i)):
        print("yes")
        break
else:
    print("No")
