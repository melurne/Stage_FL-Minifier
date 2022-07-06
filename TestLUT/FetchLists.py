import os

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

	universe.append(test)

	#individualIntersections.add(fls)

	for fl in fls.split("|") :
		if fl not in lists.keys() :
			lists[fl] = {test}
		else :
			lists[fl].add(test)

# print(list(lists.keys()))

for fl in lists.keys() :
	if os.system("cp ../Resources/filterLists/{0}/{0}.txt lists/".format(fl.replace("(", "\\(").replace(")", "\\)").replace("&", "\\&").replace("'", ""))) != 0 :
		print(fl)