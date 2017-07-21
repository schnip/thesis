def gcd(a, b):
	if (b == 0):
		return a
	if (b > a):
		return gcd(b, a)
	a = a % b
	return gcd(b, a)
