
l=[2,3,5,6]
amt=11
m=[]
for i in range(len(l)):
    m.append([0]*(amt+1))
for i in range(len(l)):
    for j in range((amt)+1):
        if j==0:
            m[i][j]=1
        elif j==l[i]:
            m[i][j]=1
        elif j<l[i]:
            m[i][j]=m[i-1][j]
        elif j>l[i]:
            m[i][j]=m[i-1][j-l[i]]
        if(m[i-1][j]==1):
            m[i][j]=1

print(m)
if(m[len(l)-1][amt])==1:
    print("yes")
else:
    print("No")
