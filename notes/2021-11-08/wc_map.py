import os
import sys
import re

import mapper_reducer


def map_it(emit, file_handle):
    pass


path = './data/books-demo'
mr = mapper_reducer.MapperReducer()
mr.map(map_it, path)
