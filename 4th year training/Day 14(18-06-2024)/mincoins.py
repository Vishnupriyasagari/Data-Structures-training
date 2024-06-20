'''
#minimum coins to get the given amount
'''
'''
c=[4,3,7]
amount=16'''
'''

a=[1,3,4,5]
amount=17
m=[]
l=[]
for i in range(len(a)):
    l=[0]*(amount)
    m.append(l)
for i in range(len(a)):
    for j in range(amount):
        if j<a[0]:
            m[i][j]=0
        if(j>=a[i]):
            m[i][j]=m[i][j-a[i]]+1           
        if (j<a[i]):
            m[i][j]=m[i-1][j]
print(m)
'''

#method 2 with list
def fun(l,n):
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if(j>=i):
                if(l1[j-i]!=-1):
                    if(l1[j]!=-1):
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-1]+1

    print(l1[-1])
l=[1,3,4,5]
n=17
fun(l,n)

