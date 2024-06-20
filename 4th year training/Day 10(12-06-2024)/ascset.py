l=[4,9,8,2,14,3,5,6]
n=len(l)
for i in range(n-2):
    if(l[i]>l[i+1]):
        l[i],l[i+1]=l[i+1],l[i]
    if(l[i+1]>l[i+2]):
            l[i+1],l[i+2]=l[i+2],l[i+1]
            if(l[i]>l[i+1]):
                 l[i],l[i+1]=l[i+1],l[i]
    print(l)
print(l)