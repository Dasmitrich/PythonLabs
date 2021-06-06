class C2:
    def __init__(self):
        self.state = 0
        # A B C D E F G H
        self.returnTable = {
            'cue':  [0, 3, 6, 8, -1, 10, -1, -1],
            'cull': [-1, 4, 5, -1, 9,  -1, -1, -1],
            'walk': [1, 2, -1, 7, -1, -1, 11, -1]
        }
        self.transitionTable = [
            {'cue': 1, 'walk': 5},  # A
            {'cull': 1, 'walk': 2, 'cue': 3},  # B
            {'cull': 3, 'cue': 0},  # C
            {'walk': 4, 'cue': 5},  # D
            {'cull': 5}, #E
            {'cue': 6}, #F
            {'walk': 7}, #G
            #H
        ]

    def evaluateState(self, funcName):
        try:
            next = self.transitionTable[self.state][funcName]
            output = self.returnTable[funcName][self.state]
            self.state = next
            return output
        except KeyError:
            raise RuntimeError()

    def cue(self):
        return self.evaluateState('cue')

    def cull(self):
        return self.evaluateState('cull')

    def walk(self):
        return self.evaluateState('walk')


o = C2()

print(o.cue())
print(o.walk())
print(o.cue())
print(o.cue())
print(o.cull())
print(o.walk())
print(o.cull())