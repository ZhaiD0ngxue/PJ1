
s='Hello\n Charlie\n Good Morning'
print(s)

s2='name \t\t age\t\t price\t\t'
s3='makr\t\t19\t\t140\t\t'
print(s2)
print(s3)

price=180
name='johe'
print('this book\'s price is %r,his dgat %s mon'    %   (price,name) )

my_valu=7.234534543
print('the value is:7.234534543')
print('the value is:%05.1fadfa'%my_valu)
print('the value is:%05.2fadfa'%my_valu)

s='1234567890'
print(s[0])
print(s[3])
print(s[-1])
print(s[-5])
print(s[1:3])
print(s[1:-2])
print(s[-5:-1])
print(s[1:])
print(s[:-1])
print(s[-5:])
print('4'in s)
print('456'in s)
print('54'in s)
print(len(s))
print(len('asdfg'))
print(max(s))
print(min(s))
print(dir(str))
print(help(str.zfill))
print(help(str.title))
print(help(str.lower))
s='asdf sdg dsgas fsSDAS dsfDFS sdfa'
print(s)
print(s.title())
print(str.title(s))
print(s.upper())
print(str.upper(s))
print(s.lower())
print(str.lower(s))
print(len(s))
print(str.strip(s))
print(len(str.strip(s)))
print(str.lstrip(s))
print(s.lstrip())
print(str.rstrip(s))
print(s.rstrip())
print(s.strip('dfa'))

print(str.startswith(s,'asdf'))
print(str.endswith(s,'fa'))
print(str.find(s,'ds',10))
print(str.index(s,'ds'))
print(s[11:13])
print(s.replace('ds','KK',2))
table={97:945}
print(s.translate(table))

table2=str.maketrans('sd','ol')
print(s.translate(table2))


print(s.split(None))
print(s.split(None,3))
s3=s.split(None)
print(":".join(s3))

