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

def isBlocked(rule, installed_lists) :
	return rule in set().union(*[[r for r in rules] for rules in installed_lists.values()])

universe, lists_dict = fetchLists()

installed_lists_names = []
installed_lists = {name: lists_dict[name] for name in installed_lists_names}

