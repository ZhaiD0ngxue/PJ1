

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



