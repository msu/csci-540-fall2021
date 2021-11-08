import os
import sys
import re

import mapper_reducer

def reduce_it(emit, key, vals):
    '''
        reduce_it is the reduce function in our map reduce algorithm

        Arguments:
        emit -- is a function to emit your output.  If you dig in, all it does
            is print to standard out, but you can just use it by calling
            ```
                emit(key, value)
            ```

        key -- the key that is being reduced for.
        values -- the values that are being reduced.  Values are strings, so
            you may need to do some casting.  For example you can cast the
            values to ints with the oneliner:
            ```
                vals_as_ints = map(int, vals)
            ```

        Example:
        To get you started, one simple example of a reduce function for counting
        words in a file, like we went over in class:
        ```
            vals_as_ints = map(int, vals)
            emit(k, sum(vals_as_ints))
        ```
    '''
    vals_as_ints = map(int, vals)
    emit(key, sum(vals_as_ints))


mr = mapper_reducer.MapperReducer()
mr.reduce(reduce_it, sys.stdin)


