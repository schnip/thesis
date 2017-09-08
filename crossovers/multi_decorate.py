from crossovers.inert import InertCrossover

class MultiDecorate():

    def __init__(self):
        self.crosser = InertCrossover()
        self.times = 2

    def setCrosser(self, c):
        self.crosser = c

    def setTimes(self, t):
        self.times = t

    def crossover(self, ind1, ind2):
        for x in range(self.times):
            (ind1, ind2) = self.crosser.crossover(ind1, ind2)
        return ind1, ind2