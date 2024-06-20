class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()
    def insert(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                t.d[i]=node()
            t=t.d[i]
        t.flag=1
    def search(self,str):
        t=self.root
        for i in str:
            if i not in t.d:
                return False
            t=t.d[i]
        if t.flag==1:
            return True
        else:
            return False
    def prefixsearch(self,str):
        t=self.root
        for i in str:
            if(i not in t.d):
                return False
            t=t.d[i]
        return True
    def prefixes(self,str):
        def fun(t,s):
            if t.flag==1:
                print(s)
                
            for i in t.d:
                fun(t.d[i],s+i)
        t=self.root
        s=''
        for i in str:
            if(i in t.d):
                s=s+i
                t=t.d[i]
            else:
                return 
        fun(t,s)
    def longprefix(self,p):
        l=[]
        
        def fun(t,s):
            if t.flag==1:
                l.append(s)
                
            for i in t.d:
                fun(t.d[i],s+i)
        for k in range(len(p)):
            str=p[k]
            t=self.root
            s=''
            for i in str:
                if(i in t.d):
                    s=s+i
                    t=t.d[i]
                else:
                    return 
            fun(t,s)
        m=len(l[0])
        for i in range(len(l)):
            if(m<len(l[i])):
                x=l[i]
        print(l)
        print(x)
            


        
t1=tries()
'''
t1.insert('word')
t1.insert('world')
print(t1.search('world'))
print(t1.prefixsearch('wo'))
'''
n=int(input())
for i in range(n):
    a,s=input().split()
    if(a=='1'):
        t1.insert(s)
    if(a=='2'):
        print(t1.search(s))
    if(a=='3'):
        print(t1.prefixsearch(s))
    if(a=='4'):
        t1.prefixes(s) #returns all the strings with given prefix
    #if(a=='5'):
        t1.longprefix(['ap','wo'])
'''
i/p :
6
1 word
1 words
2 word
op:True
3 wo
op:True
3 wa
op:False
2 wordss
op:False
#5.print the prefix from the given list who has longest string in the trie
'''