from crossovers.inert import InertCrossover

class SizeDecorate():

    def __init__(self):
        self.crosser = InertCrossover()
        self.maxLen = 1000000

    def setCrosser(self, c):
        self.crosser = c

    def setMaxLen(self, l):
        self.maxLen = l

    def crossover(self, ind1, ind2):
        (a, b) = self.crosser.crossover(ind1, ind2)
        if (len(a[0]) > self.maxLen):
            a[0] = a[0][:self.maxLen]
        if (len(b[0]) > self.maxLen):
            b[0] = b[0][:self.maxLen]
        return a, b