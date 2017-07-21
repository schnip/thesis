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