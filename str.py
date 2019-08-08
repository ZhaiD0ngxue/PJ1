
str1='charlie'
str2="翟东雪"
print(str1,str2)

str3='adfsadgsadfsdf\'sdasgfddasd\'fs gadfasdf'
print(str3 ,end='\n')


str4="jintian" 'hahaha'
print(str4)

str5=str2 + str3
print(str5)

s1='the text is '
p1=59

print(type(s1),type(p1))

# print(s1+p1)
print(s1+str(p1))
print(s1+repr(p1))

st='hahahah'
print(st)
print(repr(st))
print(str(st))

# msg1=input("qingshuru1")
# print(msg1,type(msg1))

str6='''
str6sadfag
 dsafas'asfdasffa' sdafsdf \
 asdfdsf"dsagafd"asdfas
 gdstr6     
'''
print(str6,type(str6))

num=30+34 / 23+3
print(num)

s2=r'c\gsads\fdds\t'
print(s2,type(s2))
s3=r'let''\'s go ,sdgasdf'
print(s3,type(s3))


b1=bytes()
b2=b''
b3=b'hello'
print(b3,b3[0],b3[2:4],type(b3))
b4=bytes('hahaha',encoding='utf-8')
print(b4,type(b4))
b5="sdfasdfsdf".encode('utf-16')
print(b5,type(b5))
bd=b5.decode('utf-16')
print(bd)







