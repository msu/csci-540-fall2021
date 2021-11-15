import os
import sys
import re

import mapper_reducer


def reduce_it(emit, key, vals):
    emit(key, len(vals))



mr = mapper_reducer.MapperReducer()
mr.reduce(reduce_it, sys.stdin)


