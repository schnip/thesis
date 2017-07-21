from function_library import FunctionLibrary
from fitness.test_sum import SumFitness

class GcdLibrary(FunctionLibrary):

    def getFitness(self):
        fit = SumFitness()
        return fit