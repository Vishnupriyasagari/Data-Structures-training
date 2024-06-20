class node:
    def __init__(self,u):
        self.data=u
        self.nxt=None
class sll:
    def __init__(self):
        self.head=None
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end=" ")
            t=t.nxt
        print()
    def addatend(self,x):
        t=self.head
        while(t.nxt!=None):
            t=t.nxt
        t.nxt=node(x)
    def addeven(self):
        t=self.head
        s=0
        while(t.nxt!=None):
            if(t.data%2==0):
                s+=t.data
            t=t.nxt
        print(s)
    def addfront(self,x):
        t=node(x)
        t.nxt=self.head
        self.head=t
    def search(self,x):
        f=0
        t=self.head
        while(t.nxt!=None):
            if(x==t.data):
                f=1
            t=t.nxt
        if(f==1):
            print("found")
        else:
            print("Not found")
    def middle(self):
        
        slow,fast=self.head,self.head
        while((fast!=None) and (fast.nxt!=None)):
            slow=slow.nxt
            fast=fast.nxt.nxt
        print(slow.data)
    def eo(self):
        fast=self.head
        c=0
        while(fast!=None and fast.nxt!=None):
            fast=fast.nxt.nxt
            c+=1
        if(c%2==0): #if(fast==None): even else:odd
            print("even")
        else:
            print("odd")
    def lngstg(self):
        t=self.head
        c,max1=1,0
        while(t.nxt!=None):
            if(t.nxt.data-t.data==1):
                c+=1
                if(c>max1):
                    max1=c
            else:
                c=1
            t=t.nxt
        
        print(max1)
    def pairs(self):
        t=self.head
        while(t.nxt!=None):
            t1=t.nxt
            if t1!=None:
                while(t1!=None):
                    print(t.data,t1.data)
                    t1=t1.nxt
            t=t.nxt
    def bsort(self):
        '''
        t=self.head
        while(t.nxt!=None):
            f=0
            t1=t.nxt
            while(t1!=None):
                if(t.data>t1.data):
                    f=1
                    t.data,t1.data=t1.data,t.data
                t1=t1.nxt
            if(f==0):
                break
            t=t.nxt

            '''
        t=self.head
        p=None
        while(t.nxt!=None):
            f=0
            t1=self.head
            while(t1.nxt!=p):
                if(t1.data>t1.nxt.data):
                    f=1
                    t1.data,t1.nxt.data=t1.nxt.data,t1.data
                t1=t1.nxt
            if(f==0):
                break
            p=t1
            t=t.nxt
        l1.display()
    def rev(self):
        curr=self.head
        prev=None
        while(curr):
            temp=curr.nxt
            curr.nxt=prev
            prev=curr
            curr=temp
        self.head=prev
        





          
        


l1=sll()
l1.head=node(3)
l1.addatend(2)
l1.addatend(6)
            
l1.addatend(8)

l1.display()
l1.addeven()
l1.addfront(17)
l1.display()

l1.search(34)
l1.search(12)
l1.addatend(10)
l1.display()

l1.display
l1.middle()
l1.addatend(9)
l1.addatend(2)
l1.display()
l1.middle()

l1.display()
l1.eo()
#length of ll is even or odd
l1.lngstg()
l1.pairs()
l1.display()
l1.bsort()
l1.rev()
l1.display()

