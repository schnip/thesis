from mutators.scramble import ScrambleMutator
import random
import string

class ReasonableMutator(ScrambleMutator):

    def getRandomChar(self):
        return "a"