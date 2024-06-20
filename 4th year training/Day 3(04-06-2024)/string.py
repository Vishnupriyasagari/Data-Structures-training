#s="bcdmnwc,9","khoor,5","bvec,4"
#97-122(a-z)
#65-90(A_Z)
'''
s="bvec"
k=30
res=''
k=k%26
for i in range(len(s)):
    if((ord(s[i])-k)<97):
        res=res+chr(ord(s[i])-k+26)
    else:
        res=res+chr(ord(s[i])-k)
print(res)

#length of longest substring who has alphabet in sequence
s="abcde"
c,max1=1,0
for i in range(1,len(s)):
    if((ord(s[i]))-ord(s[i-1])==1):
        c=c+1
        if c>max1:
            max1=c 
    else:
        c=1
print(max1)
'''
#ip:3 xyz pqr abc "yraxpazr"
#op:yes
n=int(input())
l=[]
l1=[]
for i in range(n):
    l.append(input())
s=input()
c=0
s1=""
for i in range(len(s)):
    j=i%n
    if(s[i] not in l[j]): 
        c=1
        break
    else:
        l1=list(l[j])
        l1.remove(s[i])
        l[j]=l1
if c==1:
    print("no")
    print(l)
else:
    print("yes")
    print(l)
'''
method2:
n=int(input())
l=[]
for i in range(n):
    l.append(list(input()))
s=input()
c=0
s1=""
for i in range(len(s)):
    j=i%n
    if(s[i] not in l[j]): 
        c=1
        break
    else:      
        l[j].remove(s[i])       
if c==1:
    print("no")
    print(l)
else:
    print("yes")
    print(l)
'''




