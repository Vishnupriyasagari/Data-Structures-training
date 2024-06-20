'''
s="MMMFFMFFMFFFF"
c1,c2=0,0
for i in range(len(s)):
    if s[i]=="M":
        c1+=1
    c2+=1
if(c1==c2):
    print("0")
elif c1>c2:
    print("M")
else:
    print("F")
'''
'''
#s=input()
s='leet**co*de*e'
b=[]
for i in s:
    if i!='*':
        b.append(i)
    else:
        b.pop()      
print("".join(b))
'''
#1859
#s="is2 sentence4 This1 a3"

