from crossovers.inert import InertCrossover
from crossovers.string_splice import StringSpliceCrossover
from mutators.inert import InertMutator
from mutators.scramble import ScrambleMutator
from fitness.inert import InertFitness

class FunctionLibrary():

	def generateStarters(self):
		return ""

	def getMutator(self):
		return ScrambleMutator()

	def getCrossover(self):
		return StringSpliceCrossover()

	def getFitness(self):
		return InertFitness()