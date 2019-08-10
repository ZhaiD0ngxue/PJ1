#if control

# s_age=input("please input your age")
age=18
if age>20:
    print("hahahahaha,20多岁的人了")
    print('hahah呀'*3)
else:
    print("you so young")
print('end')

s=None
if not s :
    print('空字符串')
else:
    print("非空")

age=35
assert 20<age<60
print('中年人')

while age < 40:
    print("grow up")
    age+=1
print(age)

tup=('q','w','e','for','ha','t')
i=0
while i<len(tup):
    print(tup[i])
    i+=1
tup=list(range(100))
# print(tup)
i=0
_list1=[]
_list2=[]
_list3=[]
while len(tup):
    tmp=tup.pop()
    if tmp%4 ==1 :
        _list1.append(tmp)
    elif tmp%4 ==2 :
        _list2.append(tmp)
    else:
        _list3.append(tmp)

print(_list1)
print(_list2)
print(_list3)
print(tup)

Value=100
sum=1
i=None
for i in range(1,Value+1):
    sum *= i
    print(sum)


for i in range(1,5):
    # i=20
    print(i)

tup=tuple(range(100))
for i in tup:
    print(i)

l1=list(range(1,100+1))
sum=0
for ele in l1:
    if isinstance(ele,int):
        sum+=ele

print(sum)
print(sum/len(l1))

for i in range(0,len(l1)):
    print('第%d个元素数值是%s'% (i,l1[i]))


score={'chinese':18,'math':50,'english':95}

for k,v in score.items():
    print('key:',k)
    print('value:',score[k])

# for k in score.keys():
#     print('keys:',k)
#
# for v in score.values():
#     print('value:',v)

print(type(score.items()))


print(l1)
zdxDict={}
for i in l1:
    if i in zdxDict:
        zdxDict[i]+=1
    else:
        zdxDict[i]=1
print(zdxDict)

######