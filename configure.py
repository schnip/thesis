f = open('main.ini', 'w')

def writeln(str):
	f.write(str)
	f.write("\n")

writeln("[genetics]")
writeln("gen_count = 1000")
f.close()