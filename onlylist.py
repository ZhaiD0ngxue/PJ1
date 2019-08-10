#only list study

tmpTuple=tuple(range(10))
aList=list(tmpTuple)
print(aList)
aList=list(range(1,10,3))
print(aList)
tmpTuple=tuple(aList)
print(tmpTuple)

aList.append('hello')
print(aList)
aList.append(tmpTuple)
aList.append(list(tmpTuple))
aList.append(range(5))
print(aList)
aList.extend(tmpTuple)
aList.extend(list(tmpTuple))
aList.extend(range(5))
print(aList)
clist=list(range(1,8))
print(clist)
print('*'*50)
clist.insert(0,'三')
clist.insert(2,tuple(aList))
print(clist,clist.index(2))

#del

del clist[2]
print(clist)

name='lalla'
print(name)
del name
# print(name)
print(clist.count(19))
print(clist.index(4))
clist.remove('三')
# clist.clear()
# del clist
print(clist)
# clist[2:4]=['三','四','?']
print(clist)
print(dir(list))
# clist.reverse()
clist.sort(reverse=False)
print(clist)
print(clist.pop())



