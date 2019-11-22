
f= open("mydate.txt",mode="r",buffering=1)

date = f.readlines()

print(date)

f.close()