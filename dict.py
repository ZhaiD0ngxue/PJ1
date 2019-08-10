#dict

score={'chinese':18,'math':50,'english':95}
print(score)
empty={}
print(empty)
dict2={(20,30):'good',40:'nice'}
print(dict2)


vegetable=[('dabaic','nanchi'),('huluobo','buhaochi'),('hongshaorou','haibucuo')]
dVegetable=dict(vegetable)
print(dVegetable)
dict3=dict(PE=80,art=90)
print(dict3)

print(score['math'])
score['physical']=60
print(score['physical'])
print(score)
del score['math']
print(score)
dict3['art']=85
print(dict3)

print('PE'in dict3)
print('art'in score)
print(dVegetable)
dVegetable.clear()
print(dVegetable)

print(dict3.get('math'))
print(score)
score.update({'social':70,'chinese':102})
print(score)
print(score.items(),'\n',score.keys(),'\n',score.values())
items=list(score.items())
keys=score.keys()
values=score.values()
print(items[1])
print(score.pop('physical'))
print(score)



cars={'BMW':8.5,'BENS':9,'AUDI':4}
print(cars)
cars.setdefault('toyota',50)
cars.setdefault('BMW',41)
print(cars)

adict=dict.fromkeys(('a','b','c'),'hahah')
print(adict)


tmp ='书名是 %(name)s,价格是 %(price)d元'
book = {'name':'今天是个好日子','price':50}
# print(tmp)
# print(book)
print(tmp % book)






