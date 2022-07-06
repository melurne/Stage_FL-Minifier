import os
for lst in os.listdir("lists") :
	old = open("lists/{}".format(lst), "r")
	new = open("uncommentedLists/{}".format(lst), "w+")
	for line in old.readlines() :
		line = line.replace("\t", "")
		if (line[0] not in {"!", "[", "\n"}) and (not (line[0] == "#" and line[1] == " "))  :
			new.write(line)
	old.close()
	new.close() 