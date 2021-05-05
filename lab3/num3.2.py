class C32:
    def __init__(self):
        self.state = 0
        # A B C D E F G H
        self.returnTable = {
            'build': [0, ],
            'split': [],
        }
        self.transitionTable = [
            {'build': 0, 'split': 1},  # A
            {'build': 2},  # B
            {'split': 4, 'build': 3},  # C
            {'build': 5, 'split': 6},  # D
            {'split': 5}, #E
            {'split': 8}, #F
            {'split': 9}, #G
            {'build': 10, 'split': 11} #H
        ]

    def evaluateState(self, funcName):
        try:
            next = self.transitionTable[self.state][funcName]
            print('n', next)
            output = self.returnTable[funcName][self.state]
            self.state = next
            return output
        except KeyError:
            raise RuntimeError()

    def build(self):
        return self.evaluateState('build')

    def split(self):
        return self.evaluateState('split')


o = C32()
print(o.build())
print(o.build())