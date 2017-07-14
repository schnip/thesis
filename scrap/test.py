def gcd(a, b):
	if (b == 0):
		return a
	if (b > a):
		return gcd(b, a)
	a = a % b
	return gcd(b, a)


import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
print(gcd(a,b))
from deap import tools
print(tools.cxTwoPoint([1,1,1,1,1,1],[2,2,2,2,2,2]))