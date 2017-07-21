from function_library import FunctionLibrary
from fitness.fish_sticks import FishSticksFitness
from fitness.test_sum import SumFitness

expr="""
def foo():
   print("hello world")

foo()
"""

class StringModLibrary(FunctionLibrary):

	def getFitness(self):
		fit = SumFitness()
		fit.addInputOutputTest([], "fish sticks", False)
		return fit
		# return FishSticksFitness()
	
	# p=ast.parse(expr)

	def generateStarters(self):
		return expr # Either original piece of code or modified