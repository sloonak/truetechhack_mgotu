import pickle
import numpy as np
d={}
d['data']= [np.array([2, 5, 3], dtype=np.int8), np.array([4, 1, 9], dtype=np.int8)]
with open('outp', 'wb') as fo:
    pickle.dump(d, fo, 2)