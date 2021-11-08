import os
import sys
import re

import mapper_reducer


def reduce_it(emit, key, vals):
    pass


mr = mapper_reducer.MapperReducer()
mr.reduce(reduce_it, sys.stdin)


