#2
import os

repository=dict()
shopList=[]

def initRepository():
    goods1=('1001','讲义1',100)
    goods2=('1002','讲义2',200)
    goods3=('1003','大法好',300)
    goods4=('1004','5年高考3年模拟',1)
    repository[goods1[0]]=goods1
    repository[goods2[0]]=goods2
    repository[goods3[0]]=goods3
    repository[goods4[0]]=goods4

def showGoods():
    print('welcom store')
    print('%13s%40s%12s'%('SN','NAME','Price'))
    for good in repository.values():
        print('%15s%40s%12s'%good)

def showList():
    print('*'*100)
    if not shopList:
        print("请选购")
    else:
        title='%-5s|%15s|%40s|%10s|%4s|%10s'%('ID','SN','Name','单价 ','count','sum')
        print(title)
        print('-'*100)

        zdxSum=0
        for i ,item in enumerate(shopList):
            id=i+1
            code=item[0]
            name=repository[code][1]
            price=repository[code][2]
            number=item[1]
            amount=price*number
            zdxSum=zdxSum+amount
            line = '%-5s|%15s|%40s|%10s|%4s|%10s'%('ID','SN','Name','单价 ','count','sum')
            print(line)
            print('-'*100)
            print('                                        总计：',zdxSum)
        print('='*100)


def add():
    code=input('please input SN code')
    if code not in repository:
        print("illeague code")
        return
    goods=repository.get(code)
    num=int(input('how many'))
    shopList.append([goods,num])

def edit():
    id=int(input('q请输入要修改的SN'))
    index=id-1
    num=int(input('要修改的shul'))
    shopList[index][1]=num

def delete():
    id=int(input("要删除的ID"))
    index=id-1
    del shopList[index]

def payment():
    showList()
    print('\n'*3)
    print('欢迎下次光临')
    os._exit(0)

cmdDict={'a':add ,'e':edit,'d':delete ,'p':payment ,'s':showGoods }
def showCmd():
    Cmd=input('请输入操作指令 \n'+'添加a \t 修改e\t 删除d\t 结算p\t 超市物品s\n')

    if Cmd not in cmdDict:
        print('hahaha,again')
    else:
        cmdDict[Cmd]()






initRepository()
showGoods()
while True:
    showList()
    showCmd()