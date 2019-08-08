
user_name='zdx'
user_age=18

print("姓名",user_name,"年龄",user_age,sep='|')

print(40,'\t',end='')
print(50,'\t',end='')
print(80,'\t')

#f=open('poem.txt','w')
#print('12345',file=f)
#print('asdfg',file=f)

import keyword

print(keyword.kwlist)

a=234
print(a)
print(type(a))
a=999999999999999999999999999999999999999999999
print(a)
print(type(a))
a=None
print(a)
print(type(a))

hax_value1=0x13
print(hax_value1)
hax_value2=0xaf
print(hax_value2)
bin_value1=0b111
print(bin_value1)
bin_value2=0b101
print(bin_value2)
oct_value1=0o54
oct_value2=0o17
print(oct_value1,oct_value2)


one_million=1_000_000
print(one_million)

price=234_567_890
print(price)

af1=5.234
print(af1)

af2=25.345
print(type(af2))

af3=25e3
print(af3)
print(type(af3))
