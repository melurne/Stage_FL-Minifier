class Group(object):
	Groupes = []
	def __init__(self):
		self.fls = set({})
		self.rules = set({})
		#Group.Groupes.append(self)

	def addFL(self, name, rules) :
		self.fls.add(name)
		for rule in rules :
			self.rules.add(rule)

	def addMultipleFLs(self, names, rules) :
		for name in names :
			self.fls.add(name)
		for rule in rules :
			self.rules.add(rule)

	def isIn(self, rule) :
		return rule in self.rules

def fuse(groupes) :
	outG = Group()
	for g in groupes :
		outG.addMultipleFLs(g.fls, g.rules)
	return outG

csvPath = "/home/maxence/StageInria/Stage_FL-Minifier/Resources/network_rules.csv"

universe = []
lists = dict({})

intersections = set({})

with open(csvPath, "r") as f :
	lines = f.readlines();

for i, line in enumerate(lines[1:-1]) :
	#print(i)
	fls = line.split("\"")[-2]
	test = line.split("|")[1]

	universe.append(test)

	for fl in fls.split("|") :
		if fl not in lists.keys() :
			lists[fl] = {test}
		else :
			lists[fl].add(test)

for fl, rules in zip(list(lists.keys()), list(lists.values())) :
	if len(Group.Groupes) == 0 :
		Group.Groupes.append(Group())
		Group.Groupes[-1].addFL(fl, rules)
	else :
		found = False
		for g in Group.Groupes :
			if len(rules.intersection( g.rules)) != 0 :
				print("f", end=' ')
				g.addFL(fl, rules)
				found = True
		if not found :
			Group.Groupes.append(Group())
			Group.Groupes[-1].addFL(fl, rules)


print()

for g in Group.Groupes :
	print(g.fls)
	print('\n')