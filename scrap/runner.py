import sys
from capturing import Capturing
def run_single(args, result):
	sys.argv = ['test.py'] + args
	with Capturing() as output:
		execfile('test.py')
