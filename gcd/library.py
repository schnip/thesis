from function_library import FunctionLibrary
from fitness.test_sum import SumFitness

class GcdLibrary(FunctionLibrary):

    def getFitness(self):
        fit = SumFitness()
        fit.addInputOutputTest([13, 13], "13", True)
        fit.addInputOutputTest([37, 600], "1", True)
        fit.addInputOutputTest([20, 100], "20", True)
        fit.addInputOutputTest([624129, 2061517], "18913", True)
        return fit

    def generateStarters(self):
        with open("gcd/buggy.py") as startingCode:
            return startingCode.read()