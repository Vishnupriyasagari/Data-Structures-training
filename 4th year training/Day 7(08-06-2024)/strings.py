'''
input:
2
polikujmnhytgbvfredcxswqaz
abcd
o/p;bdca
qwryupcsfoghjkldezxvbintma
ativedoc
o/p:codevita
'''
n=int(input())
while(n):
    a=input()
    c=input()
    s=''
    for i in a:
        if(i in c):
            s=s+(i*c.count(i))
    print(s)
    n=n-1
