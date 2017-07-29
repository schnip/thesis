f = open('main.ini', 'w')

default = """[genetics]
gen_count = 1000
pop_size = 300

[output]
filename = code
fileext = .out.py

[modules]
library = gcd.library

[input]
file = gcd/buggy.py
"""

f.write(default)
f.close()