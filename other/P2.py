# Task 1
class Node(object):
    def __init__(self):
        pass

    def resolve(self, array):
        pass


class EndNode(Node):
    def __init__(self, result):
        super().__init__()
        self.result = result

    def resolve(self, array):
        return self.result


class MidNode(Node):
    def __init__(self, array_place: int, child_nodes: dict):
        super().__init__()
        self.child_nodes = child_nodes
        self.array_place = array_place

    def resolve(self, array):
        temp = array[self.array_place]
        node = self.child_nodes.get(str(array[self.array_place]))
        return node.resolve(array)


def f21(data):
    n1: Node = MidNode(4, {"e": EndNode(0), "golo": EndNode(1)})
    n2: Node = MidNode(4, {"e": EndNode(2), "golo": EndNode(3)})
    n12: Node = MidNode(0, {"genie": n1, "tcl": n2, "pawn": EndNode(4)})

    n3: Node = MidNode(3, {"1986": EndNode(5), "2009": EndNode(6), "2002": EndNode(7)})
    n13: Node = MidNode(4, {"e": n3, "golo": EndNode(8)})

    n12_13: Node = MidNode(2, {"1971": n12, "1967": n13, "1995": EndNode(9)})

    root_node: Node = MidNode(1, {"1967": n12_13, "2008": EndNode(10), "2007": EndNode(11)})
    return root_node.resolve(data)


# Task 2
def f22(arg):
    result: hex = 0x00000000
    result |= (arg & 0xff000000)
    result |= ((arg & 0x00ff8000) >> 15)
    result |= ((arg & 0x00007fff) << 9)
    return result


# Task 3
import re

DATE_TEMPLATE = "^\d{2}\.\d{2}.\d{4}$"
PERCENT_TEMPLATE = "^\d{1,}%$"
EMAIL_TEMPLATE = "^[^@]+@[^@]+\.[^@]+$"
BOOL_TEMPLATE = "(^false$)|(^true$)"


def process_email(email):
    return str.split(email, "@")[0]


def process_percent(percent):
    return str(round(float(percent[:-1]) / 100., 1))


def process_date(date):
    date = str.split(date, '.')
    return str.format("{0}/{1}/{2}", date[0], date[1], (date[2])[2:])


def process_bool(bool):
    if str.__eq__(bool, "true"):
        return "Выполнено"
    else:
        return "Не выполнено"


def delete_row(table, row):
    table.pop(row)


def delete_column(table, column):
    for i in table:
        i.pop(column)


def delete_duplicates(table):
    if len(table) > 0:
        # deleting empty columns
        check = 0
        while check < len(table[0]):
            is_empty = True
            for row in table:
                if not row[check] is None:
                    is_empty = False
                    break
            if is_empty:
                delete_column(table, check)
            check += 1
        # deleting duplicated columns
        current = 0
        while current < len(table[0]) - 1:
            check = current + 1
            while check < len(table[0]):
                is_same = True
                counter = 0
                while counter < len(table):
                    if not str.__eq__(table[counter][check], table[counter][current]):
                        is_same = False
                        break
                    counter += 1
                if is_same:
                    delete_column(table, check)
                check += 1
            current += 1
        # deleting duplicated rows
        current = 0
        while current < len(table) - 1:
            check = current + 1
            while check < len(table):
                is_same = True
                counter = 0
                while counter < len(table[check]):
                    if not str.__eq__(table[current][counter], table[check][counter]):
                        is_same = False
                        break
                    counter += 1
                if is_same:
                    delete_row(table, check)
                check += 1
            current += 1


def reformat(table):
    result = []
    for i in range(0, len(table[0])):
        result.append([])

    for row in range(0, len(table)):
        for column in range(0, len(table[0])):
            value = table[row][column]
            if not (value is None):
                if re.fullmatch(EMAIL_TEMPLATE, str(value)) is not None:
                    value = process_email(value)
                elif re.fullmatch(PERCENT_TEMPLATE, str(value)) is not None:
                    value = process_percent(value)
                elif re.fullmatch(DATE_TEMPLATE, str(value)) is not None:
                    value = process_date(value)
                elif re.fullmatch(BOOL_TEMPLATE, str(value)) is not None:
                    value = process_bool(value)
            result[column].append(value)
    return result


def f23(table):
    delete_duplicates(table)
    table = reformat(table)
    return table
