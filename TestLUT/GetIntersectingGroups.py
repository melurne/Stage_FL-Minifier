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

for name, rules in zip(list(lists.keys()), list(lists.values())) :
	print(len(Group.Groupes), end=' ')
	foundGroupes = set({})
	for rule in rules :
		for g in Group.Groupes :
			if g.isIn(rule) :
				foundGroupes.add(g)
	if len(foundGroupes) == 0 :
		Group.Groupes.append(Group())
		Group.Groupes[-1].addFL(name, rules)
	elif len(foundGroupes) == 1 :
		list(foundGroupes)[0].addFL(name, rules)
	else :
		newG = fuse(foundGroupes)
		newG.addFL(name, rules)
		for g in foundGroupes :
			Group.Groupes.remove(g)
		Group.Groupes.append(newG)

print()

for g in Group.Groupes :
	print(g.fls)
	print('\n')