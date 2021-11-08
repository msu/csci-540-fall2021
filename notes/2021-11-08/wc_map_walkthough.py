import os
import sys
import re

import mapper_reducer

def map_it(emit, file_handle):
    '''
        map_it is the map function in our map reduce algorithm

        Arguments:
        emit -- is a function to emit your output.  If you dig in, all it does
            is print to standard out, but you can just use it by calling
            ```
                emit(key, value)
            ```

        file_handle -- file handle form which to receive input.  You can use it
            as an iterable. For example, to print every line in the input file:
            ```
                for line in file_handle:
                    print(line)
            ```

        Example:
        To get you started, one simple example of a map function for counting all
        words in a file, like we went over in class:
        ```
            for line in file_handle:
                for w0 in line.split():
                    w = re.sub('[^a-z]', '', w0.lower())
                    if w != '':
                        emit(w, 1)
        ```
    '''
    for line in file_handle:
        for w0 in line.split():
            w = re.sub('[^a-z]', '', w0.lower())
            if w != "":
                emit(w, 1)

path = './data/books-demo'
mr = mapper_reducer.MapperReducer()
mr.map(map_it, path, omit=['omit-me.txt'])
