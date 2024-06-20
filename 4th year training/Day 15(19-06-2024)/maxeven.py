a='tu5g8k1h3'
b='g5g2gd1h6'
s=[]
z=''
for i in a:
    if i.isdigit():
        if int(i) not in s:
            s.append(int(i))
for i in b:
    if i.isdigit():
        if int(i) not in s:
            s.append(int(i))
s.sort(reverse=True)
print(s)
c=0
if(s[-1]%2==1):
    for i in range(len(s)-2,-1,-1):
        if(s[i]%2==0):
            x=s[i]
            s.remove(x)
            s.append(x)
            break
        else:
            c+=1
    if(c==len(s)-1): 
        print("-1") 
    
    else:    
        
        print(*s)
        for i in range(len(s)):
            z=z+str(s[i])
        num=int(z)
        print(num)

