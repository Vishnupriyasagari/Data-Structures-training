'''l=list(map(int,input().split()))

n=len(l)
m=n//2
s=set(l)

print(s)
c=0
for i in s:
    if(l.count(i)>m):
        c+=1
print(c)

a=[4,2,4,4,8,8,4]
c=1
w=a[0]
for i in range(1,len(a)):
    if(a[i]==w):
        c+=1
    else:
        c-=1
        if(c==0):
            c=1
            w=a[i]
print(w)
'''
n=7
a=[0,5,3,6,7,2,1]
'''
for i in range(n+1):
    if(i not in a):
        print(i)
        break
'''
'''
#method 2
b=sum(a)
n=(n*(n+1))//2
print(n-b)
'''
'''
#kth largest factor of the given number
num=int(input())
k=int(input())
c=0
for i in range(num,0,-1):
    if(num%i==0):
        c+=1
        if(k==c):
            print(i)
            break
'''
'''

#coprime or not
num1=int(input())
num2=int(input())
c=0
n=(min(num1,num2))
for i in range(1,n+1):
    if(num1%i ==0 and num2%i==0):    #math.gcd(a,b)==1
        c+=1
if(c==1):
    print("coprime")
else:
    print("Not coprime")
'''
s1=input()
s=['(','[','{']
stk=[]
        
for i in range(len(s1)):
    if(s1[i] in s):
        stk.append(s1[i])
    else:
        if(stk[-1]=='(' and s1[i]==')'):
            stk.pop()
        elif(stk[-1]=='[' and s1[i]==']'):
            stk.pop()
        elif(stk[-1]=='{' and s1[i]=='}'):
            stk.pop()
        else:
            print(i+1)
            break
else:
    if(len(stk)==0):
        print(-1)











