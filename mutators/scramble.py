import random

class ScrambleMutator():
	def getRandomChar(self):
		return chr(random.randint(0, 127))

	def addChar(self, str):
		if len(str) < 1: 
			return "" + self.getRandomChar() + ""
		index = random.randint(0, len(str)-1)
		return str[:index] + self.getRandomChar() + str[index:]

	def delChar(self, str):
		if len(str) < 2: 
			return ""
		index = random.randint(0, len(str)-1) 
		return str[:index] + str[index+1:]

	def changeChar(self, str):
		if len(str) < 1: 
			return ""
		index = random.randint(0, len(str)-1)
		return str[:index] + self.getRandomChar() + str[index+1:]

	def noChange(self, str):
		return str

	def mutate(self, individual):
		changeFunc = random.choice((self.addChar, self.delChar, self.changeChar, self.noChange))
		individual[0] = changeFunc(individual[0])
		return individual, # TODO make this actually mutate the code