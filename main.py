import random, ast, sys, io
from deap import creator, base, tools, algorithms
from contextlib import redirect_stdout
from difflib import SequenceMatcher

from function_library import FunctionLibrary
from crossovers.inert import InertCrossover
from crossovers.string_splice import StringSpliceCrossover

fl = FunctionLibrary()
cr = InertCrossover()
cr = StringSpliceCrossover()

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

expr="""
def foo():
   print("hello world")

foo()
"""
p=ast.parse(expr)

def generateStarters():
	return expr # Either original piece of code or modified

toolbox.register("attr_bool", fl.generateStarters) # Starting code
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Things that do the random modifications

def getRandomChar():
	return chr(random.randint(0, 127))

def addChar(str):
	if len(str) < 1: 
		return "" + getRandomChar() + ""
	index = random.randint(0, len(str)-1)
	return str[:index] + getRandomChar() + str[index:]

def delChar(str):
	if len(str) < 2: 
		return ""
	index = random.randint(0, len(str)-1) 
	return str[:index] + str[index+1:]

def changeChar(str):
	if len(str) < 1: 
		return ""
	index = random.randint(0, len(str)-1)
	return str[:index] + getRandomChar() + str[index+1:]

def noChange(str):
	return str

def codeMutator(individual):
	changeFunc = random.choice((addChar, delChar, changeChar, noChange))
	individual[0] = changeFunc(individual[0])
	return individual, # TODO make this actually mutate the code

toolbox.register("evaluate", fl.fitnessFunction)
toolbox.register("mate", cr.crossover)
toolbox.register("mutate", codeMutator)
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