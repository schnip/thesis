from function_library import FunctionLibrary
from fitness.test_sum import *
from crossovers.line_splice import LineSpliceCrossover
from crossovers.space_splice import SpaceSpliceCrossover
from mutators.reasonable_scramble import ReasonableMutator
import configparser

pst = """


import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
print(gcd(a,b))
"""

config = configparser.ConfigParser()
config.read("main.ini")

class Library(FunctionLibrary):

    def getFitness(self):
        fit = SumFitness()
        fit.csvOutputInput("gcd/tests.csv", numDistCompare)
        fit.addValidateTest()
        # fit.addInputOutputTest([13, 13], "13", True)
        # fit.addInputOutputTest([37, 600], "1", True)
        # fit.addInputOutputTest([20, 100], "20", True)
        # fit.addInputOutputTest([624129, 2061517], "18913", True)
        fit.setPostpend(pst)
        return fit

    def generateStarters(self):
        with open(config["input"]["file"]) as startingCode:
            return startingCode.read()

    def getCrossover(self):
        return SpaceSpliceCrossover()

    def getMutator(self):
        return ReasonableMutator()