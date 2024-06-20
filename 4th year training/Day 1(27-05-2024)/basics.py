'''
#ip:300 400 count of numbers divisible by 7, with in the given range
a=300
b=400
c=0
#print((b//7)-(a//7))
for i in range(a,b):
    if i%7==0:
        c=c+1
print(c)

#if it is prime print it, if not print the next prime
def prime(a):
    c=0
    for i in range(2,(a//2)+1):
        if(a%i==0):
         c=c+1
    if(c==0):
       print(a)
    else:
        prime(a+1)
a=int(input())
prime(a)

#count of prime digits in the given number
#ip:7654
#method 1
n=int(input())
k=0
while n>0:
    rem=n%10
    c=0
    for i in range(2,(rem//2)+1):
        if(rem%i==0):
            c+=1
    if(c==0):
        k+=1
    n=n//10
print(k)  

#method 2:
n=467765
c=0
while(n):
    if(n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)
''' 
#string validation 
#ip:asd123!@#  op:1
#ip:123456789 op:3
#ip:ab op:6
s=input()
l,u,d,sc=0,0,0,0
c=0
for i in s:
    if(i.islower()):
        l=1
    if(i.isupper()):
        u=1
    if(i.isdigit()):
        d=1
    if(not i.isalnum()):
        sc=1
if l==0:
    c=c+1
if u==0:
    c=c+1
if d==0:
    c=c+1
if sc==0:
    c=c+1
#c=4-(u+d+l+sc)
if len(s)>=8: 
    if(l!=0 and u!=0 and d!=0 and sc!=0):
        print("-1")
    else:     
        print(c)
elif len(s)<8:
    if(len(s)+c>=8):
        print(c)
    elif len(s)+c<8:
        print(8-len(s))
    else:      
        print(8-len(s)+c)




