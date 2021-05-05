def f23(table_list):

    new1_list = []
    for i in range(len(table_list)):
        new1_list.append([])
        for j in range(len(table_list[i])):
            if table_list[i][j] != None and table_list[i][j] != table_list[i][j - 1]:
                new1_list[i].append(table_list[i][j])

    new1_list.remove([])
    new_list = []
    new_list.append([])
    new_list[0].append(new1_list[0][0])
    new_list[0].append(new1_list[0][1])
    new_list[0].append(new1_list[0][2])
    new_list[0].append(new1_list[0][3])

    m = 0
    for i in range(len(new1_list)):
        chck = True
        for k in range(len(new_list)):
            if new1_list[i][0] == new_list[k][0]:
                chck = False
        if chck:
            m += 1
            new_list.append([])
            for j in range(len(new1_list[i])):
                new_list[m].append(new1_list[i][j])


    num_empty = 0
    for i in range(len(new_list)):
        if not new_list[i]:
            num_empty += 1

    for i in range(num_empty):
        new_list.remove([])

    table_transponded = []

    for i in range(len(new_list)):
        if new_list[i][1] == '1':
            new_list[i][1] = 'Y'
        elif new_list[i][1] == '0':
            new_list[i][1] = 'N'

        tab1 = str(new_list[i][0]).split(' ')
        new_list[i][0] = tab1[1] + ' ' + tab1[0]

        tab = str(new_list[i][2]).split('.')
        new_list[i][3] = round(float(new_list[i][3]), 1)
        new_list[i][2] = tab[2] + '-' + tab[1] + '-' + tab[0]
        new_list[i][3] = str(new_list[i][3])

    for i in range(len(new_list[i])):
        table_transponded.append([])
        for j in range(len(new_list)):
            if j < len(new_list) and i < len(new_list[0]):
                table_transponded[i].append(new_list[j][i])

    return table_transponded


f23([['Зомегянц Святослав', '1', None, '2001.05.25', '0.333', '0.333'],
 ['Гумевич Валерий', '1', None, '2001.12.16', '0.332', '0.332'],
 [None, None, None, None, None, None],
 ['Тобечев Максим', '0', None, '2000.02.20', '0.541', '0.541'],
 ['Зомегянц Святослав', '1', None, '2001.05.25', '0.333', '0.333'],
 ['Бамочян Захар', '1', None, '1999.04.04', '0.929', '0.929'],
 ['Зомегянц Святослав', '1', None, '2001.05.25', '0.333', '0.333']])