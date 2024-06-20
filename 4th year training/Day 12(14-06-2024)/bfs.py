
def bfs(s):
    v=[]
    q=[s]
    while q:
        for i in graph[q[0]]:
            if i not in q and i not in v:
                q.append(i)
        v.append(q.pop(0))
    print(v)

graph={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2,12],3:[5,7,8],2:[4,8,9],12:[8,1],9:[2],1:[12]}
bfs(5)
