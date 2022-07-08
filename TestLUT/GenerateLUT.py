import random

def fetchLists() :
	csvPath = "/home/maxence/StageInria/Stage_FL-Minifier/Resources/network_rules.csv"

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
		if i >= 20000 :
			subset_candidate = unused
		# print(subset_candidate.keys())
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
			valid = True

		if i >= 20000 :
			return subset_candidate

	return subset_candidate

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

n = 11

universe, lists_dict = fetchLists()

# print(createValidSubset(lists_dict, n, lists_dict))

subsets = decomposeLists(lists_dict, n)
for s in subsets :
	print(len(list(s.keys())))