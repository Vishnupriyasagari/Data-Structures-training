
'''
l=[2,3,4,1,3,2,4,2,1,3]
c=0
l2=[]
n=len(l)
while(c!=len(l)):
    l1=[]
    for i in range(len(l)):
        if(l[i]>0):  #if(not str(a[i]).isalpha()):
            if l[i] not in l1:
                c+=1
                l1.append(l[i])
                l[i]=-1      #a[i]='a'
    l2.append(l1)
print(l2)
'''
'''
#method 2 using dictionary
l=[2,3,4,1,3,2,4,2,1,3]
d={}
c=0
l2=[]
for i in l:
    if(i not in d):
        d[i]=1
    else:
        d[i]=d[i]+1
while(c!=len(l)):
    l1=[]
    for i in d:
        if(d[i]!=0):
            d[i]=d[i]-1
            c=c+1
            l1.append(i)
    l2.append(l1)

print(l2)
'''
'''
a="The quikk brown fox jumps over the lazy dog"
b=''
print(b)
c=a.lower()
c1=0
a1="abcdefghijklmnopqrstuvwxyz"
for i in range(len(c)):
    if a[i]!=' ' and c[i] not in b and c[i].lower() not in b:
        b=b+c[i]
print(b)
for i in a1:
    if i not in b:
        print("No")
        break
    else:
        c1=1
else:
    if(c1!=0):
        print("yes")
'''
#method2
a=input()
b=97
for i in range(b,123):
    if(chr(i) not in a):
        print("No")
        break
else:
    print("yes")

#method3
a=input()
d={}  #d=set(d)    #d3.=[0]*26
for i in a:
    if(i.islower()):
        if i not in d:
            d[i]=1   #d.add(i) #3.d[ord(i)-97]=1
if(len(d)==26):  #3.print(all(d))
    print("yes")
else:
    print("No")