import re
import datetime


class Table:
    def __init__(self, name, num0, date, num1, num2):
        self.name = name
        self.num0 = num0
        self.date = date
        self.num1 = num1
        self.num2 = num2

    def __str__(self):
        return format(self.name, self.num0, self.date, self.num1, self.num2)

    def __eq__(self, other):
        if isinstance(other, Table):
            return (self.name == other.name and
                    self.num0 == other.num0 and
                    self.date == other.date and
                    self.num1 == other.num1 and
                    self.num2 == other.num2)
        return NotImplemented

    def getName(self):
        return self.name

    def getNum0(self):
        return self.num0

    def getDate(self):
        return self.date

    def getNum1(self):
        return self.num1

    def getNum2(self):
        return self.num2


newTable = []
nameTable = []
surnameTable = []
sexTable = []
dateTable = []
numTable = []


def restruct():

    for i in range(len(newTable)):
        nameTable.append(newTable[i].getName())

    for i in range(len(newTable)):
        surnameTable.append(newTable[i].getNum0())

    for i in range(len(newTable)):
        sexTable.append(newTable[i].getDate())

    for i in range(len(newTable)):
        dateTable.append(newTable[i].getNum1())

    for i in range(len(newTable)):
        numTable.append(newTable[i].getNum2())


def prnt():
    for i in range(len(nameTable)):
        print('|' + nameTable[i], end='')
        print(' ' + surnameTable[i], end='|')

    print('\n' + '-' * len(newTable)*16)

    for i in range(len(sexTable)):
        print('|' + sexTable[i] + '|', end='\t\t\t\t\t')

    print('\n' + '-' * len(newTable)*16)

    for i in range(len(dateTable)):
        print('|' + dateTable[i] + '|', end='\t')

    print('\n' + '-' * len(newTable)*16)

    for i in range(len(numTable)):
        print('|' + numTable[i] + '|', end='\t\t\t\t')


def sort():
    i = 0

    while i < len(newTable) - 1:

        if newTable[i] == newTable[i + 1] and i < len(newTable):
            del newTable[i]
            # print('done')
        else:
            i += 1


def f23():
    string = input('Enter info: ').split()

    if 6 > len(string) > 1:

        if len(string) == 5:

            string[2] = "Y" if string[2] == '1' else "N"
            newTable.append(Table(string[0], string[1], string[2], re.sub('\.', '-', str(string[3])), str(string[4])[0:3]))

            # print(newTable[0])
            f23()
        else:
            return -1

    elif string[0].__eq__('print'):
        sort()
        restruct()
        prnt()

    else:
        return 0


f23()

'''
Валерий Андреев 1 22.08.2001 0.376
Николай Васин 1 21.04.1989 0.477
Кондратий Теркин 0 22.02.1999 0.877
'''