import random

class SpaceSpliceCrossover():
	
	def noCross(self, ind1, ind2):
		return ind1, ind2

	def randomCross(self, a, b):
		ia = random.randint(0, len(a)-1) if len(a) > 1 else 0
		ib = random.randint(0, len(b)-1) if len(b) > 1 else 0
		while (a[ia:ia+1].isspace()):
			ia = ia + 1
		while (b[ib:ib+1].isspace()):
			ib = ib + 1
		na = a[:ia] + b[ib:]
		nb = b[:ib] + a[ia:]
		return na, nb

	def controlledCross(self, a, b):
		i = random.randint(0, min(len(a),len(b)))
		ia = i
		ib = i
		while (a[ia:ia+1].isspace()):
			ia = ia + 1
		while (b[ib:ib+1].isspace()):
			ib = ib + 1
		na = a[:ia] + b[ib:]
		nb = b[:ib] + a[ia:]
		return na, nb

	def crossover(self, ind1, ind2):
		# print(ind1)
		crossFunc = random.choice((self.noCross, self.controlledCross, self.randomCross))
		(a,b) = crossFunc(ind1[0], ind2[0])
		ind1[0] = a
		ind2[0] = b
		return ind1, ind2