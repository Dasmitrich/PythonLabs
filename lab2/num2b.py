
def f22(x):
    D = (x & 0x80000000) >> 31
    C = (x & 0x7f800000) >> 22
    B = (x & 0x007f0000) >> 7
    A = (x & 0x0000ffff) << 16
    return hex(A | B | C | D)


f22(0x03853219)
#0x03853219