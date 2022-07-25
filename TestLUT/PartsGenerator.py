from itertools import combinations
import multiprocessing as mp
import time

def fetchLists() :
	csvPath = "/home/maxence/StageInria/Stage_FL-Minifier/Resources/network_rules.csv"
	# csvPath = "./network_rules.csv"
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
	if set() not in subset_candidate.values() and not (len(set().union(*list(subset_candidate.values()))) < len(subset_candidate)) :
		# print(subset_candidate)
		# print({key: lists_dict[key] for key in subset_candidate.keys()})
		return True
	else :
		return False

def run(part) :
	global lists_dict
	# global gen
	global unused
	global subsets
	# global progress

	# print(part)
	# progress.value += 1
	# print(progress.value, end='\r')
	if validateSubset(lists_dict, part) :
		subsets.append(part)
		for l in part.keys():
			if l in unused :
				del[unused[l]]


def testParts(lists_dict, n) :
	# global gen
	global unused
	subsets = []
	gen = generateParts(unused, n)
	i = 0
	with mp.Pool(processes = 3) as pool :
		start = time.time()
		pool.map(run, gen)
		end = time.time()
		print('time = {}'.format(end-start))

def decompose(lists_dict) :
	for i in [1, 2, 3] :
		print("------------------", i)
		testParts(lists_dict, i)

universe, lists_dict = fetchLists()

with mp.Manager() as manager :
	# gen = manager.dict()
	subsets = manager.list([])
	unused = manager.dict({key: value for key, value in lists_dict.items()})
	progress = mp.Value('i', 0)

	decompose(lists_dict)
	for s in subsets :
		print(len(list(s.keys())))
	with open("testRunParts3.txt", "w+") as f :
		for s in subsets :
			f.write("\n")
			for l, rules in s.items() :
				f.write("{0} : {1} - {2}\n".format(l, rules, "True" if len(rules) < len(lists_dict.values()) else "False"))
