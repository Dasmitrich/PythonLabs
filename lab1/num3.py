
def f13(n, m):

    part_a = 0
    for i in range(1, n+1):
        part_a += 32 * i ** 8 + i ** 6

    part_b = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            part_b += 49 * j ** 4 + i ** 2

    return part_a - part_b


float(f13(66, 53))
