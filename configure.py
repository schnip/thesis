f = open('main.ini', 'w')

def writeln(str):
	f.write(str)
	f.write("\n")

writeln("[genetics]")
writeln("gen_count = 1000")
writeln("pop_size = 300")
writeln("")
writeln("[output]")
writeln("filename = code")
writeln("fileext = .out.py")
writeln("")
writeln("[modules]")
writeln("library = gcd.library")
f.close()