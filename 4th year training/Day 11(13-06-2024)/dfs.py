'''

def dfs(s,l):
    l.append(s)
    
    for i in graph[s]:
        if i not in l:
            dfs(i,l)
    return l

graph={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
print(dfs(5,[]))
'''
'''
#all possible paths
def dfs(s,l,e):
    l.append(s)
    if(s==e):
        print(l)
        l.pop()
        return
    for i in graph[s]:
        if i not in l:
            dfs(i,l,e)
    l.pop()
graph={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
dfs(5,[],2)'''
'''
#all cost
def dfs(s,l,e,sum1):
    l.append(s)
    if(s==e):
        print(l,'-',sum1)
        sum1=0
        l.pop()
        return
    for i,cost in graph[s]:
        if i not in l:
            dfs(i,l,e,sum1+cost)
    l.pop()

graph={5:[(7,2),(3,4)],
       7:[(5,2),(4,1),(3,2)],
       4:[(7,1),(8,1),(2,3)],
       8:[(3,3),(4,1),(2,5)],
       3:[(5,4),(7,2),(8,3)],
       2:[(4,3),(8,5)]}
dfs(5,[],2,0)
'''
'''
#least cost path
def dfs(s,l,e,sum1,m,m1):   
    l.append(s)
    if(s==e):
        if(m>sum1):
            m=sum1
            m1=l.copy()
        #print(l,'-',sum1)
        sum1=0
        l.pop()
        return m,m1        
    for i,cost in graph[s]:
        if i not in l:
            m,m1=dfs(i,l,e,sum1+cost,m,m1)
    l.pop()
    return m,m1

graph={5:[(7,2),(3,4)],
       7:[(5,2),(4,1),(3,2)],
       4:[(7,1),(8,1),(2,3)],
       8:[(3,3),(4,1),(2,5)],
       3:[(5,4),(7,2),(8,3)],
       2:[(4,3),(8,5)]}
print(dfs(5,[],2,0,9999,[]))
'''
'''
#printing all the possible paths
def dfs(s,l,e):
    l.append(s)
    if(s==e):
        print(l)
        l.pop()
        return
    for i in graph[s]:
        if i not in l:
            dfs(i,l,e)
    l.pop()
graph={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
for i in graph:
    dfs(5,[],i)
'''
#from starting nodes to other nodes shortest path
def dfs(s,l,e,sum1,m,m1):   
    l.append(s)
    if(s==e):
        if(m>sum1):
            m=sum1
            m1=l.copy()
        #print(l,'-',sum1)
        sum1=0
        l.pop()
        return m,m1        
    for i,cost in graph[s]:
        if i not in l:
            m,m1=dfs(i,l,e,sum1+cost,m,m1)
    l.pop()
    return m,m1

graph={5:[(7,2),(3,4)],
       7:[(5,2),(4,1),(3,2)],
       4:[(7,1),(8,1),(2,3)],
       8:[(3,3),(4,1),(2,5)],
       3:[(5,4),(7,2),(8,3)],
       2:[(4,3),(8,5)]}
for i in graph:
    print(dfs(5,[],i,0,9999,[]))


