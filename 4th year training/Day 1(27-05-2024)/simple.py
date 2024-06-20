'''
#print sorted list
l1=[2,5,7,9]
l2=[1,3,6,7,10,13]
#l1=list(map(input().split()))
l3=l1+l2
#l3.sort()
#print(l3)
#print(sorted(l1+l2))
#list,set,string,lamda fun
#i,j=0,0
i=0
j=0
c=[]
while(i<len(l1) and j<len(l2)):
    if l1[i]<l2[j]:
        c.append(l1[i])
        i=i+1
    else:
        c.append(l2[j])
        j=j+1
#if(j<len(l2)):
    #c.extend(l2[j:])
#if(i<len(l1)):
    #c.extend(l1[i:])
while(j<len(l2)):
    c.append(l2[j])
    j=j+1
while(i<len(l1)):
    c.append(l1[i])
    i=i+1
print(c)

#input:aaabbaaaaddd
#op:a3b2a4d3
s1='aaabbaaaadddb'
c=1
s=''
for i in range(len(s1)-1):
    if s1[i]==s1[i+1]:
        c=c+1  
    else:
        s=s+s1[i]+str(c)
        c=1
s=s+s1[i+1]+str(c) #s1[-1]
print(s)

#input:3 5 4 3 6 7 1 2 4 3 3 7 6 8 8
#op:3-4,5-1,4-2,6-2,7-2,1-1,8-2
#a=list(map(int,input().split('')))
a=[3,4,7,9,8,8,6,4,3,5]
b=[]
for i in a:
    if(i not in b):
        b.append(i)
print(b)
for i in b:
    print(i,"-",a.count(i))

#ip-f46feLK9y56u#@&56hIjbn6KJhA
#op-lv-,Uv,lc-,uc-,d,s-
s='f46feLK9y56u#@&56hIjbn6KJhA'
lv,uv,lc,uc,d,sc=0,0,0,0,0,0
for i in s:
    if(i.islower()):
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'): #if(i in 'aeiou')
            lv=lv+1
        else:
            lc=lc+1
    elif i.isupper():
        if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):  #if(i in 'AEIOU')
            uv=uv+1
        else:
            uc=uc+1
    elif i.isdigit():
        d=d+1
    elif(not i.isalnum()):#-for special char
        sc=sc+1
print("lv-",lv)
print("lc-",lc)
print("uv-",uv)
print("uc-",uc)
print("d-",d)
print("sc-",sc)

#ip:placements,School
#op:plAcEmEnts,schOOl
s1='placements'
s2='School'
for i in s1:
    if i in 'aeiou':
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')
print()
for i in s2:
    if i in 'aeiou':
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')
'''
#ip:5 3.8 7 5.6 4 2 3
#op:15 6 9.4
l1=list(map(float,input().split()))
e,o,f=0,0,0
for i in l1:
    if i%2==0:  #if(int(a)==a)
        e=e+i
    elif i%2==1:
        o=o+i
    else:          
        f=f+i
print("even sum = ",int(e))
print("odd sum = ",int(o))
print("float sum = ",f)




