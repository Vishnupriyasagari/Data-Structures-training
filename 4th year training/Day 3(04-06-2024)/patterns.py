'''
n=int(input())
k=1
for i in range(n):
    for j in range(n):
        if(i==0 or j==0 or i==n-1 or j==n-1):
            print("*",end=" ")
        else:
            print(k,end=" ")
            k+=1
    print()
'''
'''input:5   
o/p:
* * * * *
* 1 2 3 *
* 4 5 6 *
* 7 8 9 *
* * * * *
''' 
'''
input:4
o/p:
____a____,___aba___,__abcba__,_abcdcba_
'''
n=int(input())
a=97
for i in range(n,0,-1):
    for j in range(i-1,0,-1):
        print("_",end=" ")
    print()