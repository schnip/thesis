from fractions import gcd
import io

f = open("gen_tests.csv","w")

MAX = 27

for i in range(1,MAX):
    for j in range(1,MAX):
        f.write(str(gcd(i,j)) + "," + str(i) + "," + str(j))
        if (i < MAX and j < MAX):
            f.write("\n")

f.close()