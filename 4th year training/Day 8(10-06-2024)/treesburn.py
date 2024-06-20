#binary matrix as input where 1->tree,0->land;print no.of unburnt trees where adjacent trees can burn

def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
        
    if i<n-1:
        fun(l,i+1,j,n)  #3 bottom
    if i>0:
        fun(l,i-1,j,n)  #1 top
    if j<n-1:
        fun(l,i,j+1,n)  #4 right
    if j>0:
        fun(l,i,j-1,n)  #2 left
    
      
l=[]
n=int(input())
for i in range(n):
    l.append(list(map(int,input().split())))
c=0
r=int(input())
c1=int(input())
fun(l,r,c1,n)

for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            c+=1
print(c)

'''
i/p
6
0 1 1 1 0 1
0 1 0 1 0 0 
1 0 1 1 0 0
0 0 0 1 1 1
1 1 0 0 0 1
1 1 1 0 1 0
3,5
o/p
8'''
