from itertools import *
import sys
import random
import json
import numpy as np

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
	# csvPath = "/home/maxence/StageInria/Stage_FL-Minifier/Resources/network_rules.csv"
	csvPath = "./network_rules.csv"
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
n_lists = 20

universe = [i for i in range(n_rules)]

lists_dict = {'L{}'.format(i): set(random.sample(universe, random.randrange(0, n_rules))) for i in range(n_lists)}
lists_indexes = {'L{}'.format(i): i for i in range(n_lists)}

# universe = [i for i in range(8)]

# lists_dict = {	
# 	'L1': {0, 1, 3}, 
# 	'L2': {2, 3, 4},
# 	'L3': {0, 5, 6, 7},
# 	'L4': {1, 3}
# }
# lists_indexes = {
# 	'L1' : 0,
# 	'L2' : 1,
# 	'L3' : 2,
# 	'L4' : 3
# }
# memShrink(val)
lookuptable = {getKey(val, lists_dict) : val for val in generateValues(lists_indexes)}
# print(lookuptable)
print(sys.getsizeof(json.dumps(lookuptable)))
print(len(lookuptable))