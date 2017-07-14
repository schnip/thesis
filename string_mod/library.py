from function_library import FunctionLibrary
from fitness.fish_sticks import FishSticksFitness

expr="""
def foo():
   print("hello world")

foo()
"""

class StringModLibrary(FunctionLibrary):

	def getFitness(self):
		return FishSticksFitness()
	
	# p=ast.parse(expr)

	def generateStarters(self):
		return expr # Either original piece of code or modified