def fun(r,c,i):
    path=set()
    if i==len(word):
        return True
    if (r<0 or c<0 or r>=n or c>=n or word[i]!=l[r][c] or (r,c) in path):
        return False
    path.add((r,c))
    t=(fun(r+1,c,i+1) or fun(r-1,c,i+1) or fun(r,c+1,i+1) or fun(r,c-1,i+1))
    path.remove((r,c))
    return t   
l=[]
n=int(input())
for i in range(n):
    l.append(list(map(str,input().split(" "))))
c=0
word=input()
for i in range(n):
    for j in range(n):
        
        if fun(i,j,0):
            c=1
            print("yes")
            break
        
if(c!=1):
    print("No")
        

