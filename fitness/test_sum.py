import sys
import io
from contextlib import redirect_stdout
from difflib import SequenceMatcher
from fitness.inert import InertFitness


def executeIndividual(individual, params):
    sys.argv = params
    f = io.StringIO()
    with redirect_stdout(f):
        exec(individual)
    s = f.getvalue()
    return s

def strictCompare(a, b):
    if (a == b):
        return 1
    return 0

def looseCompare(a, b):
    return SequenceMatcher(None, a, b).ratio()

def numDistCompare(a, b):
    if ((a == "None") or (b == "None")):
        return 0
    try:
        aa = float(a)
        bb = float(b)
    except:
        return 0
    if (aa == bb):
        return 1
    return 1 - 1 / abs(aa - bb)


class SumFitness(InertFitness):

    def __init__(self):
        self.tests = []
        self.postpend = ""

    def setPostpend(self, pst):
        self.postpend = pst

    def getPostpend(self):
        return self.postpend

    def setTests(self, tsts):
        self.tests = tsts

    def addTest(self, test):
        self.tests.append(test)

    def addValidateTest(self):
        def test(individual):
            try:
                s = executeIndividual(individual[0] + self.postpend, params)
            except:
                return 0
            return 1
        self.addTest(test)

    def csvOutputInput(self, s, strict):
        with open(s) as f:
            lines = f.readlines()
        lines = [l.strip() for l in lines]
        for line in lines:
            items = line.split(",")
            out = items.pop(0)
            # print(items, out)
            self.addInputOutputTest(items, out, strict)

    def addInputOutputTest(self, inputArgs, output, compare):
        def test(individual):
            params = ['test.py'] + inputArgs
            try:
                s = executeIndividual(individual[0] + self.postpend, params)
            except:
                return 0
            return compare(s[:-1], output)
        self.addTest(test)

    def fitness(self, individual):
        sum = 0
        for test in self.tests:
            sum = sum + test(individual)
        return sum/len(self.tests),

    def isMaxFitness(self, fit):
        return fit[0] >= 1