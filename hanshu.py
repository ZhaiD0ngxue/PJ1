#function

def my_max(x,y):
    '''
    helpwendang
    '''
    #diyihang
    z= x if x >y else y
    #dierhang
    return z
    #zuihouyihang
def say_hi():
    print('=================hi=================')

a,b=12,9
print(my_max(a,b))
print(say_hi())
print('--'*100)
print(my_max.__doc__)
print('--'*100)
#print(help(my_max))
print('--'*100)


def sum_and_avg(list):
    sum=0
    count=0
    for e in list:
        if isinstance(e,int) or isinstance(e,float):
            count+=1
            sum+=e
    return sum,sum/count

myList=[23,45,65,234,65,76]
tp1=list(sum_and_avg(myList))
tp2=sum_and_avg(myList)
print(tp1,tp2)
sum,avg=tp2
print(sum,'-----------',avg)

def fn(n):
    if n==0:
        return 1
    elif n==1:
        return 4
    else:
        return 2*fn(n-1)+fn(n-2)

print(fn(10))

def say(name='defaul',ms='def msg'):
    print(name ,'说',ms)

say()
say('sunwukong','halow')
say('baigujing')
say(ms='jintiant',name='lalala') 


