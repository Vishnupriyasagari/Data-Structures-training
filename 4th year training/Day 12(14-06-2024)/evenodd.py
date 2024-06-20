def odd(x,s,j,l3,s1):   
    if j==len(l2):
        l4.append(s1)
        return l3
    if l2[j]%2==1:
        s=s+l2[j]
        l3.append(s)
        s1=s1+s    
    return odd(x,x,j+1,l3,s1)   
    
def fun(l1,l2,i,j):
    if(i==len(l1)):
        return l3        
    if(l1[i]%2==0):
        if(j!=len(l2)): 
            (odd(l1[i],l1[i],0,l3,0))          
    return fun(l1,l2,i+1,0)   
l4=[]           
l3=[]
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
print(fun(l1,l2,0,0))
print(l4)
#2 lists are given from l1, if it is even add that number with all odd numbers of l2 and append it to another list
'''
o/p:
[13, 11, 9, 15, 9, 7, 5, 11, 11, 9, 7, 13]
[48, 32, 40]
'''