import sys
import random

def gen_mat(fname, size):
    with open(fname, 'w') as f:
        for i in range(1, size):
            for j in range(1, size):
                f.write('{} {} {}\n'.format(i, j, random.random()))

if len(sys.argv) != 2:
    print("Error", sys.argv[0], "size")
size = int(sys.argv[1])

gen_mat("mat1.txt", size)
gen_mat("mat2.txt", size)

