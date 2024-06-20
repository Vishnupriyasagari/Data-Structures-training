'''
l=[3,2,5,4,1,6,8]
n=len(l)
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            print((l[i],l[j],l[k]))
'''
def subset(l,n,i,j,k):
    if(k==n-1):
        print(l[i],l[j],l[k])
        j=j+1
        k=j+1
    elif(k==n-1 and j==n-2):
        
        i=i+1
        j=i+1
        k=j+1
    elif(i==n-3 and j==n-2 and k==n-1):
        return
     
    else:
        print(l[i],l[j],l[k])
        k=k+1
        subset(l,n,i,j,k)

l=[3,2,5,4,1,6,8]
n=len(l)
i=0
j=i+1
k=j+1
subset(l,n,i,j,k)