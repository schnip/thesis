def gcd(a, b):
	if (b == 0):
		return a
	if (b > a):
		return gcd(b, a)
	return gcd(b, a)
