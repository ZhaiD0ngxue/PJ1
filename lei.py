

class Person:
    '这是学习python定义的一个PERSON类'
    hair='black'
    def __init__(self,name='charlie',age=9):
        self.name=name
        self.age=age
    def say(self,content):
        print(content)


p=Person()
print(p.name,p.age)
p.name='ligang'
p.say("haha")
print(p.name,p.age,p.hair)

p.skill='swiming'
print(p.skill)

del p.name
#print(p.name)

def info(self):
    print('-----info func------',self)

p.foo=info
p.foo(p)
p.bar=lambda self:print('lambda fun',self)
p.bar(p)

def introa(self,content):
    print('woshiyigeren,xinxiwei%s'%content)

from types import MethodType
p.intro=MethodType(introa,p)

p.intro("生活")

class Dog:
    def jump(self):
        print('---jump---  ')

    def run(self):
        self.jump()
        print('---run----')
        self.jump()

d=Dog()

d.jump()
d.run()

class InContructor:
    def __init__(self):
        foo=0
        self.foo=6

print(InContructor().foo)

class User():
    def test(self):
        print('self canshu',self)
u=User()
u.test()
foo=u.test
foo()

class ReturnSelf():
    def grow(self):
        if hasattr(self,'age'):
            self.age+=1
        else:
            self.age=1
        return self

rs=ReturnSelf()
rs.grow().grow().grow().grow()
print(rs.age)



