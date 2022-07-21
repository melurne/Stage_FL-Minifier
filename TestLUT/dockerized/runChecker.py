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

		if "EasyList" in fls :
			fls.remove("EasyList")

		universe.append(i)

		#individualIntersections.add(fls)

		for fl in fls :
			if fl not in lists.keys() :
				lists[fl] = {i}
			else :
				lists[fl].add(i)
		print(len(fls))

	return universe, lists

def fetchSubsets() :
	subsets = []
	runPath = "./testRunParts2.txt"
	with open(runPath, "r") as f :
		for line in f.readlines() :
			if line == "\n" : 
				continue
			liste, tmp = line.split(" : ")


universe, lists_dict = fetchLists()
