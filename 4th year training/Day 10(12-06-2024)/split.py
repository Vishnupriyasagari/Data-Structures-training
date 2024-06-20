a="hello:5438,car:214,book:8799,apple:2187".split(',')
c=''
print(a)
for i in a:
    b=i.split(':') 
    b[1]=list(b[1]) 
    l=len(b[0])
    if(str(l) in (b[1])):
        c=c+(b[0][-1])
    else:
        for i in range(l-1,0,-1):
            if(str(i) in b[1]):
                c=c+b[0][i-1]
                break
        else:
            c=c+'x'
    
print(c)
'''
o/p:
['hello:5438', 'car:214', 'book:8799', 'apple:2187']
oaxp length of hello is 5 , append 5th element in string, if not next smallest number index+1 element
'''           



    


