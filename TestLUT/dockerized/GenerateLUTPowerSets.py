import random
from itertools import combinations

def fetchLists() :
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

def generatesubset(unused, n) :
	if n < len(unused) :
		# un subset quelconque de unused de taille n si n < len(unused)
		subset_keys = random.sample(list(unused.keys()), n)
		subset = {key: value for key, value in unused.items() if key in subset_keys}
	else :
		subset = unused

	return subset

def createValidSubset(lists_dict, n, unused) :
	valid = False
	i = 0
	while valid == False :
		i+=1
		print(i)
		subset_candidate = generatesubset(unused, n)
		if i >= 30000 :
			subset_candidate = unused
		# print(subset_candidate.keys())
		valid = validateSubset(lists_dict, subset_candidate)

		if i >= 30000 :
			return subset_candidate

	return subset_candidate

def validateSubset(lists_dict, subset_candidate) :
	tmpSet = [rules for key,rules in lists_dict.items() if key not in subset_candidate.keys()]
	UMinusCandidate = set().union(*tmpSet)
	for l,rules in subset_candidate.items() :
		todel = []
		for rule in rules :
			if rule in UMinusCandidate :
				todel.append(rule)
		for rule in todel :
			subset_candidate[l].remove(rule)
	# print(subset_candidate)
	if set() not in subset_candidate.values() :
		return True
	else :
		return False

def decomposeLists(lists_dict, n) :
	unused = {key: value for key, value in lists_dict.items()}
	subsets = []
	while unused != dict({}) :
		subset = createValidSubset(lists_dict, n, unused)
		subsets.append(subset)
		if subset != unused :
			for l in subset.keys() :
				del[unused[l]]
		else :
			return subsets
	return subsets

def generateParts(lists_dict, n) :
	parts = combinations(list(lists_dict.keys()), n)
	return [{key: value for key, value in lists_dict.items() if key in subset_keys} for subset_keys in parts]

def testParts(lists_dict, parts) :
	i = 0
	valids = []
	print("start")
	while i < len(parts) :
		print(i)
		part = parts[i]
		if validateSubset(lists_dict, part) :
			for l in part.keys() :
				for p in parts[i:] :
					if l in p.keys() :
						parts.remove(p)
			valids.append(part)
		i+=1
	return valids

def decompose(lists_dict) :
	unused = {key: value for key, value in lists_dict.items()}
	subsets = []

	for i in [3] :
		print("------------", i)
		print("Getting powerset")
		valids = testParts(lists_dict, generateParts(unused, i))
		for p in valids[:-1] :
			for l in p.keys() :
				del[unused[l]]
			subsets.append(p)
	# for i in range(5, 10) :
	# 	print("------------", i)
	# 	# valids = testParts(lists_dict, generateParts(unused, i))
	# 	valids = decomposeLists(unused, i)
	# 	if len(valids) > 1 :
	# 		for p in valids[:-1] :
	# 		# 	for l in p.keys() :
	# 		# 		del[unused[l]]
	# 			subsets.append(p)
	# 	unused = {key: value for key, value in valids[-1].items()}

	subsets.append(unused)
	return subsets

n = 11

universe, lists_dict = fetchLists()

# print(createValidSubset(lists_dict, n, lists_dict))

subsets = decompose(lists_dict)
for s in subsets :
	print(len(list(s.keys())))

with open("results/testRunParts.txt", "w+") as f :
	for s in subsets :
		f.write("\n\n")
		for l, rules in s.items() :
			f.write("{0} : {1}\n".format(l, rules))
