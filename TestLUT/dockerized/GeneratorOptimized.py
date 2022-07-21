from itertools import combinations

def fetchLists2() :
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

def fetchLists() :
	# csvPath = "/home/maxence/StageInria/Stage_FL-Minifier/Resources/network_rules.csv"
	csvPath = "./network_rules.csv"
	universe = []
	lists = dict({})
	individualIntersections = set({})

	with open(csvPath, "r") as f :
		lines = f.readlines();

	for i, line in enumerate(lines[1:]) :
		#print(i)
		if "\"" in line :
			fls = line.split("\"")[-2].split("|")
		else :
			fls = line.split("|")[-3].split("|")
		test = line.split("|")[1]

		if "urlhaus-filter" in fls :
			fls.remove("urlhaus-filter")
		# if "Easylist" in fls :
		# 	fls.remove("Easylist")
		# if "Fanboy's_Complete_List" in fls :
		# 	fls.remove("Fanboy's_Complete_List")

		universe.append(i)

		#individualIntersections.add(fls)

		for fl in fls :
			if fl not in lists.keys() :
				lists[fl] = {i}
			else :
				lists[fl].add(i)
		# print(len(fls))

	return universe, lists

def generateParts(lists_dict, n) :
	for subset in combinations(list(lists_dict.keys()), n) :
		yield {key: set([val for val in value]) for key, value in lists_dict.items() if key in subset}

def validateSubset(lists_dict, subset_candidate) :
	tmpSet = [rules for key,rules in lists_dict.items() if key not in subset_candidate.keys()]
	UMinusCandidate = set().union(*tmpSet)
	for l,rules in subset_candidate.items() :
		# print(subset_candidate)
		todel = []
		for rule in rules :
			if rule in UMinusCandidate :
				todel.append(rule)
		for rule in todel :
			subset_candidate[l].remove(rule)
		# print(subset_candidate)
	# print(subset_candidate)
	if set() not in subset_candidate.values() :
		return True
	else :
		return False

def testParts(lists_dict, unused, n) :
	subsets = []
	generator = generateParts(unused, n)
	i = 0
	for part in generator :
		print(i, end="\r")
		i += 1
		if validateSubset(lists_dict, part) :
			subsets.append(part)
			for l in part.keys():
				del[unused[l]]
			generator = generateParts(unused, n)

	return subsets

def decompose(lists_dict) :
	unused = {key: value for key, value in lists_dict.items()}
	subsets = []
	for i in [1, 2, 3, 4] :
		print("------------------", i)
		valids = testParts(lists_dict, unused, i)
		for p in valids :
			# for l in p.keys() :
			# 	del[unused[l]]
			subsets.append(p)

	subsets.append(unused)
	return subsets

n = 11

universe, lists_dict = fetchLists()

# print(createValidSubset(lists_dict, n, lists_dict))
# print(lists_dict)
subsets = decompose(lists_dict)
for s in subsets :
	print(len(list(s.keys())))

# print(lists_dict)

with open("testRunParts3.txt", "w+") as f :
	for s in subsets :
		f.write("\n")
		for l, rules in s.items() :
			f.write("{0} : {1} - {2}\n".format(l, rules, "True" if len(rules) < len(lists_dict.values()) else "False"))

