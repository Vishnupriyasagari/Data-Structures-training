'''
there are n buildings with some heights and find the max rain water stored in between them
[2,5,2,3,6,7,1,0,5,7] o/p:20
'''
h=[2,4,2,3,4,4,1,0,5,4]
#h=[2,5,2,3,6,7,1,0,5,7]
#h=[4,3,4,5,6,1,0,6,7]
n=len(h)
minb=[]
maxb=[]
m=0
s=0
for i in range(n):
    if(h[i]>m):
        m=h[i]
    minb.append(m)
x=0
print
for i in range(n-1,-1,-1):
    if x<h[i]:
        x=h[i]
    maxb.insert(0,x)
print(minb)
print(maxb)
for i in range(n):
    s=s+(min(minb[i],maxb[i])-h[i])
print(s)


