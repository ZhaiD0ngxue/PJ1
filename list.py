#list

myList=['crazyit',30,'python']
myTuple=('tcraz',50,'jojojio','tpyth','wahaha')
print(myList,'\n',myTuple)
print(myList[0],myList[1],myList[-1])
print(myTuple[0],myTuple[2],myTuple[-2])
myTuple1=(0,1,2,3,4,5,6,7,8,9)
print(myTuple1[1:-3:3])
myTuple2=('a','b','c','d')
sumTuple=myTuple1+myTuple2
print(sumTuple)
myList1=[2,4,5,6,7,8,5]
myList2=['d','for ','e','g']
sumList=myList1+myList2
print(sumList)
print(myList1*2,myTuple2*3)

order_endings=('st','nd','rd')+('th',)*17+('st','nd','rd')+('th',)*7+('st',)
print(order_endings)
day=3
print(str(day)+order_endings[day-1])

print('asdf'in myTuple2,'d'in myTuple2,not 'b'in myTuple2)

print(myTuple1,max(myTuple1),min(myTuple1),len(myTuple1))

print('*'*50)

vals=10,20,30
print(vals,type(vals),id(vals),vals[2],len(vals))
a,b,c=vals
print(a,b,c)
aTuple=tuple(range(1,10))
print(aTuple)

a=11
b=22
c=33
abc=a,b,c
print(abc)
c,b,a=abc
print(a,b,c)
print(abc)
first,*second,reset=range(10)
print(first,'\n',second,'\n',reset)





