from itertools import *
import sys
import random
import json
import pickle
import time
import numpy as np
import matplotlib.pyplot as plt

import bitarray

class BoolArray(object):

  # create from an ndarray
  def __init__(self, array):
    ba = bitarray.bitarray()
    ba.pack(array.tobytes())
    self.arr = ba.tobytes()
    self.shape = array.shape
    self.size = array.size

  # convert back to an ndarray
  def to_array(self):
    ba = bitarray.bitarray()
    ba.frombytes(self.arr)
    ret = np.frombytes(ba.unpack(), dtype=np.bool)[:self.size]
    return ret.reshape(self.shape)

  def __cmp__(self, other):
    return cmp(self.arr, other.arr)

  def __hash__(self):
    return hash(self.arr)

def fetchLists() :
	csvPath = "/home/maxence/StageInria/Stage_FL-Minifier/Resources/network_rules.csv"
	# csvPath = "./network_rules.csv"
	universe = []
	lists = dict({})
	individualIntersections = set({})

	with open(csvPath, "r") as f :
		lines = f.readlines();

	for i, line in enumerate(lines[1:-1]) :
		#print(i)
		fls = line.split("\"")[-2]
		test = line.split("|")[1]

		universe.append(i)

		#individualIntersections.add(fls)

		for fl in fls.split("|") :
			if fl not in lists.keys() :
				lists[fl] = {i}
			else :
				lists[fl].add(i)

	return universe, lists

def generateValues(lists_indexes) : # lists_indexes = {list: index}
	i = 0
	for possibility in chain.from_iterable(combinations(list(lists_indexes.keys()), r) for r in range(len(list(lists_indexes.keys()))+1)) :
		out = [False for i in lists_indexes.keys()]
		for l in possibility :
			out[lists_indexes[l]] = True
		print(i, end='\r')
		i+=1
		yield out

def memShrink(val) :
	out = 0
	for i, status in enumerate(val) :
		if status:
			out |= 1 << i
	return out

def getKey(val, lists_dict) :
	global universe
	out = [False for i in range(len(universe))]
	# out = 0
	for i, status in enumerate(val) :
		if status:
			for r in list(lists_dict.values())[i] :
				out[r] = True
	return BoolArray(np.array(val)).__hash__()

n_rules = 12422
# n_lists = 15

universe, fullLists = fetchLists()

data = []
for n_lists in range(6, 20) :
	print("------------------", n_lists)
	lists_dict = {key: {rule for rule in fullLists[key]} for key in random.sample(list(fullLists.keys()), n_lists)}
	lists_indexes = {key: i for i, key in enumerate(list(lists_dict.keys()))}

	start = time.time()
	lookuptable = {getKey(val, lists_dict) : val for val in generateValues(lists_indexes)}
	end = time.time()

	print(sys.getsizeof(pickle.dumps(lookuptable)))
	print(len(lookuptable))
	print(end-start)
	data.append((sys.getsizeof(pickle.dumps(lookuptable))/len(lookuptable), (end-start)/len(lookuptable)))
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot([i for i in range(1, len(data)+1)], [data[i][0] for i in range(len(data))], "r+")
ax2.plot([i for i in range(1, len(data)+1)], [data[i][1] for i in range(len(data))], "b+")
plt.show()

print([data[i][0] for i in range(len(data))]) # 28 + 6.25*n2**2 bytes
print([data[i][1] for i in range(len(data))])