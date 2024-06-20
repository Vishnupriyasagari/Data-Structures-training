'''
n=7262
h=n//3600
n=n%3600
m=n//60
s=n%60
print(h,'hr:',m,'min:',s,'sec')
#op:2 hr: 1 min: 2 sec, given n in sec
'''

n=65476
y=n//360
n=n%360
m=n//30
n=n%30
w=n//6
d=n%6

print(y,"yrs",m,'m',w,'weeks',d,'days')


