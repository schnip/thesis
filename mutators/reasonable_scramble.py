from mutators.scramble import ScrambleMutator
import random
import string

class ReasonableMutator(ScrambleMutator):

    def getRandomChar(self):
        s = string.printable
        i = random.randint(0,len(s) - 1)
        return s[i:i+1]
