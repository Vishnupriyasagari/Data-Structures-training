#next nearest palindrome if the given number is not palindrome
'''
def palin(n):
    temp=n
    
    rev=0
    while n>0:
        rev=rev*10+(n%10)
        n=n//10
    if(temp==rev):
        return temp
    else:
        return palin(temp+1)
n=122
print(palin(n))
'''
'''
s=123#76541#153#1112#1234#192 #12345  #192
s=str(s)
s1=''
s2=''
if(s==s[::-1]):
    print(s)
else:
    if(len(s)%2==0):
        s1=s[:len(s)//2]
        s2=s1+s1[::-1]
        if(int(s)>int(s2)):
            s1=s[:len(s)//2]
            s1=int(s1)+1
            s1=str(s1)
            s2=s1+s1[::-1]
    else:
        s1=s[:len(s)//2+1]
        s2=s1+s1[-2::-1]
        if(int(s)>int(s2)):
            s1=str(int(s1)+1)
            s2=s1+s1[-2::-1]

print(s2)
'''
#ip:abdbsdabca
#op:bdb

def longestPalindrome(s):
    n=len(s)
    def is_palin(left,right):
        while left>=0 and right<n and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    res=""
    for i in range(len(s)):
        if len(s)==1:
            return s
        pal1=is_palin(i,i)
        if len(pal1)>len(res):
            res=pal1
        pal2=is_palin(i,i+1)
        if len(pal2)>len(res):
            res=pal2
    return res 
s='abdbsdabca'   
print(longestPalindrome(s)) 
