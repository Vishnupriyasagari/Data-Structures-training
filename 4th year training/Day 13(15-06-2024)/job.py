nums=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
for i in range(1,len(nums)):
    for j in range(0,i):
        if nums[j][1]<=nums[i][0]:
            if(b[i]<b[j]+a[i]):
                b[i]=b[j]+a[i]
print(b)
print(max(b))
'''
max price a by working in the given time slots accordingly (2,5),(5,8)-6+11=17
o/p:
[5, 6, 10, 14, 17, 16]
17
'''