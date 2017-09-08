import sys
sys.path.insert(0,'..')
from crossovers.string_splice import *
x = "abcdefghijklmnop"
y = "abcdefghijklmnop"
ssc = StringSpliceCrossover()
print(ssc.crossover([x], [y]))