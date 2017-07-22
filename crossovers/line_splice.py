import random

class LineSpliceCrossover():

    def noCross(self, ind1, ind2):
        return ind1, ind2

    def randomCross(self, a, b):
        la = a.splitlines()
        lb = b.splitlines()
        ia = random.randint(0, len(la)-1) if len(la) > 1 else 0
        ib = random.randint(0, len(lb)-1) if len(lb) > 1 else 0
        na = la[:ia] + lb[ib:]
        nb = lb[:ib] + la[ia:]
        return "\n".join(na), "\n".join(nb)

    def controlledCross(self, sa, sb):
        a = sa.splitlines()
        b = sb.splitlines()
        i = random.randint(0, min(len(a),len(b)))
        # print(a)
        # print(len(a))
        na = a[:i] + b[i:]
        nb = b[:i] + a[i:]
        return "\n".join(na), "\n".join(nb)

    def crossover(self, ind1, ind2):
        # print(ind1)
        crossFunc = random.choice((self.noCross, self.controlledCross, self.randomCross))
        (a,b) = crossFunc(ind1[0], ind2[0])
        ind1[0] = a
        ind2[0] = b
        return ind1, ind2