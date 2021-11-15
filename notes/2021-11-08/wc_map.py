import os
import sys
import re

import mapper_reducer


def map_it(emit, file_handle):
    for line in file_handle:
        for w0 in line.split():
            w = re.sub('[^a-z]', '', w0.lower())
            if w != "":
                emit(w, 1)


path = './data/books-demo'
mr = mapper_reducer.MapperReducer()
mr.map(map_it, path, omit=['omit-me.txt'])
