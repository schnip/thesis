class FishSticksFitness():
	
	def executeIndividual(self, individual, params):
		sys.argv = params
		f = io.StringIO()
		with redirect_stdout(f):
			exec(individual)
		s = f.getvalue()
		return s

	def fitness(self, individual):
		try:
			s1 = executeIndividual(individual[0], [])
		except:
			return -1,
		s0 = "\nfish sticks\n"
		ret = SequenceMatcher(None, s0, s1).ratio()
		return ret,