import matplotlib.pyplot as plt

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

#print([len(fl) for fl in lists.values()])
# todel = []
# for fl, rules in zip(lists.keys(), lists.values()) :
# 	if len(rules) == 1 :
# 		todel.append(fl)

# for fl in todel :
# 	del[lists[fl]]

values = list(lists.values())

#intersections = [[set({})]*len(values)]*len(values)
intersections = [[set({}) for i in range(len(values))] for j in range(len(values))]
fls = lists.keys()

#print([[len(intersections[i][j]) for j in range(len(intersections[i]))] for i in range(len(intersections))])


for i, fli in enumerate(lists.values()) :
	for j, flj in enumerate(lists.values()) :
		intersections[i][j] = fli.intersection(flj) 

# usefull_lists = dict({})
# simple_fls = []

# for i in range(len(intersections)) :
# 	if len(intersections[i][i]) == len(lists[list(lists.keys())[i]]) :
# 		simple_fls.append(lists[list(lists.keys())])

# len_intersections = [[len(intersections[i][j]) for j in range(len(intersections[i]))] for i in range(len(intersections))]

# for i, fl in enumerate(fls) :
# 	if sum(len_intersections[i]) == max(len_intersections[i]) :
# 		simple_fls.append(fl)
# 	else :
# 		usefull_lists[fl] = lists[fl]

# universe = []

# for l in usefull_lists.values() :
# 	for rule in l :
# 		universe.append(rule)

# for k, rule in enumerate(universe) :
# 	#n = 0
# 	#print(k)
# 	for i, fli in enumerate(usefull_lists.values()) :
# 		for j, flj in enumerate(usefull_lists.values()) :
# 			#print((rule in fli) and (rule in flj))
# 			if (rule in fli) and (rule in flj) :
# 				#n += 1
# 				intersections[i][j].add(k) 

# print(list(lists.keys()))
# for i in range(len(intersections)) :
# 	print([len(intersections[i][j]) for j in range(len(intersections[i]))])


print(list(lists.keys()))
for i in range(len(intersections)) :
	for j in range(len(intersections[i])) :
		if len(intersections[i][j]) != 0 :
			plt.plot(j, -i, marker="o", markersize=0.3, color="green")

plt.show()