from itertools import combinations

def generator(seq, r):
	if r:
		for i in range(r - 1, len(seq)):
			for cl in (list(c) for c in generator(seq[:i], r - 1)):
				cl.append(seq[i])
				yield tuple(cl)
	else:
		yield tuple()

# def generateParts(lists_dict, n) :
# 	parts = xuniqueCombinations(list(lists_dict.keys()), n)
# 	for subset in parts :
# 		yield {key: value for key, value in lists_dict.items() if key in subset}

def generateParts(lists_dict, n) :
	for subset in uniqueCombinations(list(lists_dict.keys()), n) :
		yield {key: value for key, value in lists_dict.items() if key in subset}

def uniqueCombinations(set, n) :
	for s in combinations(s, n) :
		yield s

def xuniqueCombinations(items, n):
    if n==0: 
    	yield []
    else:
        for i in range(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

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

def testParts(lists_dict, parts) :
	i = 0
	valids = []
	for part in parts :
		print(i)
		if valids != [] and set(part).intersection(*valids) != set() :
			print(valids)
			continue
		if validateSubset(lists_dict, part) :
			valids.append(part)
		i +=1
	return valids

def decompose(lists_dict) :
	unused = {key: value for key, value in lists_dict.items()}
	subsets = []
	# for i, part in enumerate(generateParts(unused, 2)) :
	# 	print(len(part.keys()))
	# 	print()
	# 	print(part.keys())
	# 	if i > 15 :
	# 		return subsets
	for i in [3] :
		valids = testParts(lists_dict, generateParts(unused, i))
		for p in valids[:-1] :
			for l in p.keys() :
				del[unused[l]]
			subsets.append(p)
	# for i in range(3, 40) :
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

with open("testRunParts2.txt", "w+") as f :
	for s in subsets :
		f.write("\n")
		for l, rules in s.items() :
			f.write("{0} : {1}".format(l, rules))