#!/usr/bin/env python

import sys
import random


def make_weights(num_assignments):
    weights = [random.random() for _ in range(num_assignments)]
    norm = sum(weights)
    return map(lambda x: x/norm, weights)


def make_assignment(aid, weight, num_student, prefix='grade', suffix='txt'):
    fname ='{}-{}.{}'.format(prefix, aid, suffix)
    with open(fname, 'w') as f:
        for i in range(num_students):
            f.write('{} {} {}\n'.format(i, weight, random.randint(40, 100)))

if len(sys.argv) != 2:
    print("Error", sys.argv[0], "num_assignments")
num_assignments = int(sys.argv[1])
num_students = 100

weights = make_weights(num_assignments)
for i, w in enumerate(weights):
    make_assignment(i, w, num_students)

