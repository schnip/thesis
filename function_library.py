from crossovers.inert import InertCrossover
from crossovers.string_splice import StringSpliceCrossover
from mutators.inert import InertMutator
from mutators.scramble import ScrambleMutator

class FunctionLibrary():
	def executeIndividual(self, individual, params):
		sys.argv = params
		f = io.StringIO()
		with redirect_stdout(f):
			exec(individual)
		s = f.getvalue()
		return s

	def fitnessFunction(self, individual):
		try:
			s1 = executeIndividual(individual[0], [])
		except:
			return -1,
		s0 = "\nfish sticks\n"
		ret = SequenceMatcher(None, s0, s1).ratio()
		return ret,

	def crossOver(self, ind1, ind2):
		return ind1, ind2

	def generateStarters(self):
		return ""

	def getMutator(self):
		return ScrambleMutator()

	def getCrossover(self):
		return StringSpliceCrossover()