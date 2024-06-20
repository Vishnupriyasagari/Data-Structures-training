class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def addback(self,x):
        if(self.head==None):
            self.head=Node(x)
            self.tail=self.head
        else:
            t=Node(x)
            self.tail.next=t
            t.prev=self.tail
            self.tail=t
    def addfront(self,x):
        if(self.head==None):
            self.head=Node(x)
            self.tail=self.head
        else:
            t=Node(x)
            t.next=self.head
            self.head.prev=t
            self.head=t
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next 
        print()
    def revdis(self):
        t=self.tail
        while(t!=None):
            print(t.data,end="->")
            t=t.prev 
        print()
    def search(self,x):
        t1=self.head
        t2=self.tail
        while(t1!=t2 and t1!=t2.next):
            if(t1.data==x or t2.data==x):
                print("found")
                break
            t1=t1.next
            t2=t2.prev
        else:
            if(t1.data==x):
                print("found")
            else:

                print("Not found")
    def eolen(self):
        t1=self.head
        t2=self.tail
        while(t1!=t2 and t1!=t2.next):
            t1=t1.next
            t2=t2.prev
        if(t1.data==t2.data):
            print("Odd")
        else:
            print("even")
    def palin(self):
        t1=self.head
        t2=self.tail
        f=0
        while(t1!=t2 and t1!=t2.next):
            if(t1.data==t2.data):
                t1=t1.next
                t2=t2.prev
            else:
                f=1
                break
        if(t1.data==t2.data and f==0):
            print("palindrome")
        else:
            print("Not a palindrome")
    def halfswap(self):
        
        slow=self.head
        fast=self.head
        while(fast!=None):
            slow=slow.next
            fast=fast.next.next
        self.tail.next=self.head
        self.head.prev=self.tail
        t1=slow.prev
        t1.next=None
        slow.prev=None
        self.head=slow
        self.tail=t1
        '''
        t=self.head
        t1=slow.data
        print(slow.data)
        while(t1!=None):
            t.data,t1.data=t1.data,t.data
            t1=t1.next
            t=t.next
            '''
    def swapalternate(self):
        '''
        t=self.head
        while(t!=None and t.next!=None):
            t.data,t.next.data=t.next.data,t.data
            t=t.next.next
        '''
        t=self.head
        t1=self.head.next
        t3=None
        c=0
        while(t!=None):
            t.next=t1.next
            t1.next=t
            t1.prev=t3
            t.prev=t1
           
            if(c==0):
                self.head=t1
                c=1
            else:
                t3.next=t1
            t,t1=t1,t
            t3=t1
            
            if(t1.next!=None):
                t1=t1.next.next
            t=t.next.next
    def validpar(self):
        s=['(','[','{']
        stk=[]
        t=self.head
        i=0
        while(t!=None):     
            if(t.data in s):
                stk.append(t.data)
            else:
                if(stk[-1]=='(' and t.data==')'):
                    stk.pop()
                elif(stk[-1]=='[' and t.data==']'):
                    stk.pop()
                elif(stk[-1]=='{' and t.data=='}'):
                    stk.pop()
                else:
                    print(i+1)
                    break
            i=i+1   
            t=t.next
        if(len(stk)==0):
            print(-1)
    def eosdiff(self,x,es,os):
        if(x==None):
            return abs(es-os)
        if(x.data%2==0):
            es+=x.data
        elif(x.data%2==1):
            os+=x.data
        x=x.next
        return self.eosdiff(x,es,os)
    
    def primec(self,x,c): 
        def prime(y,i):  
            if(y==1):
                return 0
            if i==(y//2)+1:
                return 1
            if y%i==0:
                return 0
            return prime(y,i+1)
        if(x==None):
            return c
        y=x.data
        if(prime(y,2)):
            c+=1
        x=x.next
        return self.primec(x,c)
    
 
      
l1=dll()

l1.addfront(7) 
l1.addfront(1) 
l1.addfront(8)
l1.addfront(2)
l1.addfront(6)  
l1.addfront(5) 
l1.addfront(11) 
l1.addfront(3) 
l1.display() 
'''l1.revdis()
l1.search(300)
l1.eolen()
l1.palin()
l1.display()
l1.halfswap() 
l1.display() 
l1.swapalternate()     
l1.display() 
#l1.validpar()'''
#print(l1.eosdiff(l1.head,0,0))
print(l1.primec(l1.head,0))
