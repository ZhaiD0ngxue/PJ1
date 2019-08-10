
#运算符
st='python \t'
pi='3.14'
pi2=float(pi)+1
vasiab=True
str2=st
print(st,pi,vasiab,str2,pi2)

a=-7.2
b=4.7
theSum=a+b
print(theSum)
print(st+pi)
theMinus=a-b
print(theMinus)
c=-0.4
print(-c)
print(+b)
print(a*b)
print(b*c)
print(a**b)

st2=st*3
print(st2)

print(a/b)
print(a//b)
print(a//1)

print(a%b)
print('%.3f' % (-5.2%1.5))

print(8**(1/3))
print(9**(1/2))

st='0123456789'
print(st[2:9:2])
print(st[2:9:3])

print(5>4)
print(5>=5)
print(5<4)
print(5<=5)
print(5==4)
print(5==5)
print(5!=4)
print(5!=5)
print(5is 4)
print(5is 5)
print(int(True))
print(int(False))
print(True+True)
# print(True/False)
import time

a=time.gmtime()
b=time.gmtime()
print(a,b)
print(id(a),id(b))
print(a==b)
print(a is b)

print(not False,not True)
print( not (5<3 or 5<4))

print('zhende' if 5<4 else 'jiade')
s='asdgwersdgaf'
print('sd'in s)
print("sd"not in s)

sIndex=input('loation')
sChar=input('char')
print(s.replace(s[int(sIndex)],sChar))




