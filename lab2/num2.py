import re


def numCheck(num):
    Num = ''
    temp = ''

    if num[0] > '8':
        n = 1
    else:
        n = 2

    for i in range(n):
        if '8' > num[i] > '3':
            temp += '0'

        elif '4' > num[i] > '1':
            temp += '00'

        elif num[i] == '1':
            temp += '000'

        elif num[i] == '0':
            temp += '0000'

        else:
            Num = str(bin(int(num, 16)))
            Num = re.sub(r'0b', '', Num)

    Num = str(bin(int(num, 16)))
    Num = re.sub(r'0b', '', Num)
    Num = temp + Num

    return Num


def f22(num):

    num = re.sub(r'0x', '', num)
    Num = int(num, 16)

    D = Num >> 31
    D = str(D)

    Num = numCheck(num)
    # print(Num)

    C = Num[1:9]
    # print(C)

    B = Num[9:16]
    # print(B)

    A = Num[16:32]
    # print(A)

    res = B
    return bin(int(res, 2))


print(f22('0x7050cb10'))
