import os
import sys
import re
import json

class MapperReducer(object):

    def _emit(self, k, v):
        print(k, ":", json.dumps(v))

    def map(self, mapfunc, path, omit=["gen.py"]):
        for fname in os.listdir(path):
            if fname in omit:
                continue

            file_name = os.path.join(path, fname)
            with open(file_name, 'r') as f:
                mapfunc(self._emit, f)

    def reduce(self, reducefunc, f):
        cur_key, cur_val = None, []
        for line in f:
            k, v = line.strip().split(" : ")
            v = json.loads(v)
            if k != cur_key:
                if cur_key is not None:
                    reducefunc(self._emit, cur_key, cur_val)
                cur_key, cur_val = k, [v]
            else:
                cur_val.append(v)
        reducefunc(self._emit, cur_key, cur_val)
