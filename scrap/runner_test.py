# import sys
# from capturing import Capturing
# sys.argv = ['gcd.py', '12', '123']
# with Capturing() as output:
# 	execfile('gcd.py')
# print('the output is', output)
# print(int(output[0]) + 1)

import sys
import io
from contextlib import redirect_stdout

sys.argv = ['gcd.py', '12', '123']
f = io.StringIO()
with redirect_stdout(f):
	with open('gcd.py') as source_file:
		exec(source_file.read())
		# help(pow)
s = f.getvalue()
print(s)