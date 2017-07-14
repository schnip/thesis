import random, ast, sys, io
from deap import creator, base, tools, algorithms
from contextlib import redirect_stdout
from difflib import SequenceMatcher

from function_library import FunctionLibrary

fl = FunctionLibrary()
cr = fl.getCrossover()
mu = fl.getMutator()
# cr = InertCrossover()
# cr = StringSpliceCrossover()
# mu = InertMutator()
# mu = ScrambleMutator()

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

expr="""
def foo():
   print("hello world")

foo()
"""
# p=ast.parse(expr)

def generateStarters():
	return expr # Either original piece of code or modified

toolbox.register("attr_bool", fl.generateStarters) # Starting code
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", fl.fitnessFunction)
toolbox.register("mate", cr.crossover)
toolbox.register("mutate", mu.mutate)
toolbox.register("select", tools.selTournament, tournsize=3) # I don't think there is anything that is specific to the data

population = toolbox.population(n=300)

NGEN=100
for gen in range(NGEN):
	print(gen)
	offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
	fits = toolbox.map(toolbox.evaluate, offspring)
	for fit, ind in zip(fits, offspring):
		ind.fitness.values = fit
	population = toolbox.select(offspring, k=len(population))
top10 = tools.selBest(population, k=1)
for i in top10:
	print("result", fl.fitnessFunction(i),i)
f = open('outfile.txt', 'w')
f.write("# The best fitness found was: " + str(fl.fitnessFunction(top10[0])[0]))
f.write("\n# ======================================\n")
f.write(str(top10[0][0]))
f.close()