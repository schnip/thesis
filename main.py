import io
import configparser
import importlib
from deap import creator, base, tools, algorithms
from pylab import *

from function_library import FunctionLibrary
from string_mod.library import StringModLibrary

config = configparser.ConfigParser()
config.read("main.ini")

library_module = importlib.import_module(config["modules"]["library"])
lib = library_module.Library()
cr = lib.getCrossover()
mu = lib.getMutator()
fn = lib.getFitness()

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", lib.generateStarters)  # Starting code
toolbox.register("individual", tools.initRepeat,
				 creator.Individual, toolbox.attr_bool, n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", fn.fitness)
toolbox.register("mate", cr.crossover)
toolbox.register("mutate", mu.mutate)

# I don't think there is anything that is specific to the data
toolbox.register("select", tools.selTournament, tournsize=3)

population = toolbox.population(n=int(config["genetics"]["pop_size"]))

NGEN = int(config["genetics"]["gen_count"])
fitChart = []
escape = False
bestFit = None
bestFitness = 0
for gen in range(NGEN):
	print(gen, bestFitness)
	fitChart[gen] = bestFitness
	bestFit = None
	bestFitness = 0
	offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
	fits = toolbox.map(toolbox.evaluate, offspring)
	for fit, ind in zip(fits, offspring):
		if fn.isMaxFitness(fit):
			print("DONE")
			escape = True
		if fit[0] > bestFitness:
			bestFitness = fit[0]
			bestFit = ind
		ind.fitness.values = fit
	population = toolbox.select(offspring, k=len(population))
	if escape:
		break
top10 = tools.selBest(population, k=1)
for i in top10:
	print("result", fn.fitness(i), i)
f = open(config["output"]["filename"] + config["output"]["fileext"], 'w')
f.write("# The best fitness found was: " + str(fn.fitness(top10[0])[0]))
f.write("\n# ======================================\n")
f.write(str(top10[0][0]))
f.write(fn.getPostpend())
f.close()

plot(range(NGEN), fitChart)
show()