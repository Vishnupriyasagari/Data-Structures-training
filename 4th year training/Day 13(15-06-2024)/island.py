def fun(l,i,j,n,c):
    if l[i][j]==0:
        return c
    if l[i][j]==1:
        
        l[i][j]=0
        c=c+1
        
    if i<n-1:
        c=fun(l,i+1,j,n,c)
    if i>0:
        c=fun(l,i-1,j,n,c)
    if j<n-1:
        c=fun(l,i,j+1,n,c)
    if j>0:  
        c=fun(l,i,j-1,n,c) 
    return c
l=[]

m1=0
n=int(input())
for i in range(n):
    l.append(list(map(int,input().split())))
count=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:

            count+=1
          
            m=fun(l,i,j,n,0)
            
            if(m>m1):
                m1=m
print("number of islands:",count)
print('largest area:',m1)


'''
i/p
5
0 0 0 0 0
0 1 1 0 0
0 1 1 1 0
1 0 0 0 0
1 1 1 0 0
o/p:
number of islands: 2
largest area: 5
'''
