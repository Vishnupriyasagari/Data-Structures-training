def maxim(l1):
    if len(l1)==0:
        return 0
    if(len(l1)==1):
        return l1[0]
    if(len(l1)==2):
        return max(l1)
    left=l1[0]+maxim(l1[2:])
    right=l1[1]+maxim(l1[3:])  
    return max(left,right)   
l=[13,9,4,10,5,7]
m=maxim(l)
print(m)