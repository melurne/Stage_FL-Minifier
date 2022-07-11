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

		universe.append((i, test))

		#individualIntersections.add(fls)

		for fl in fls.split("|") :
			if fl not in lists.keys() :
				lists[fl] = {i}
			else :
				lists[fl].add(i)

	return universe, lists

