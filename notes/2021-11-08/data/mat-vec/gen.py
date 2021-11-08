import sys
import random

if len(sys.argv) != 2:
    print("Error", sys.argv[0], "size")
size = int(sys.argv[1])

with open('vec.txt', 'w') as f:
    for i in range(1, size):
        f.write('{} {}\n'.format(i, random.random()))

with open('mat.txt', 'w') as f:
    for i in range(1, size):
        for j in range(1, size):
            f.write('{} {} {}\n'.format(i, j, random.random()))

