#1
#divide
def divide(num):
    zdxZhenshu=int(num)
    zdxXiaoshu=num - zdxZhenshu
    return (str(zdxZhenshu),str(zdxXiaoshu))

hanList=['零','一','二','三','四','五','六','七','八','九']
unitList=['十','百','千','万']

def four_to_hanstr(num_str):
    result=''
    num_len=len(num_str)
    for i in range(num_len):
        num=int(num_str[i])
        if i != num_len-1 and num !=0:
            result+=hanList[num]+unitList[num-2-i]
        else:
            result+=hanList[num]

    return result

def int_to_str(num_str):
    str_len=len(num_str)
    if str_len > 12:
        print("too large ")
        return
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8])+ '亿' + four_to_hanstr(num_str[-8:-4]) +'万'+ four_to_hanstr(num_str[-4:])
    elif str_len > 4:
        return four_to_hanstr(num_str[-8:-4]) +'万'+ four_to_hanstr(num_str[-4:])
    else:
        return four_to_hanstr(num_str)

num=float(input("请输入一个浮点数"))
integer,fraction=divide(num)

print(int_to_str(integer))


