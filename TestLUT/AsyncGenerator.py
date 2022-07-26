from itertools import combinations
import multiprocessing as mp
import asyncio
from threading import Thread
from queue import Queue
import itertools
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

async def worker(GenQ, ResQ) :
	_ , lists_dict = fetchLists()
	while True :
		part = await GenQ.get()

		if part == 'close' :
			await ResQ.put('close')
			return


		if validateSubset(lists_dict, part) :
			await ResQ.put(part)

async def Producer(GenQ, unused, n) :
	i = 0
	lists = {key: value for key, value in unused.items()}
	for part in generateParts(lists, n) :
		print(i, end='\r')
		i+=1
		try :
			GenQ.put_nowait(part)
		except asyncio.QueueFull :
			await GenQ.put(part)
	for _ in range(4) :
		await GenQ.put('close')
	return

async def producerTee(GenQ, iterator) :
	i = 0
	for part in iterator :
		print(i, end='\r')
		i+=1
		await GenQ.put(part)
	for _ in range(4) :
		await GenQ.put('close')
	return

async def Producer_old(part) :
	global GenQ
	GenQ.put(part)

async def updator(ResQ, unused, subsets) :
	while True :
		part = await ResQ.get()
		if part == 'close' :
			return
		for l in part.keys():
			if l in unused :
				del[unused[l]]
		if len(part) > 0 :
			subsets.append(part)

async def main(unused, subsets, i) :
	GenQ = asyncio.Queue(500)
	ResQ = asyncio.Queue(200)
	
	# it1, it2 = itertools.tee(generateParts(unused, i), 2)
	# print(type(it1))
	# prod1 = asyncio.create_task(producerTee(GenQ1, it1))
	# prod2 = asyncio.create_task(producerTee(GenQ2, it2))
	prod = asyncio.create_task(Producer(GenQ, unused, i))
	upda = asyncio.create_task(updator(ResQ, unused, subsets))

	W1 = asyncio.create_task(worker(GenQ, ResQ))
	W2 = asyncio.create_task(worker(GenQ, ResQ))
	W3 = asyncio.create_task(worker(GenQ, ResQ))
	W4 = asyncio.create_task(worker(GenQ, ResQ))

	await prod
	# await prod1
	# await prod2
	await upda
	await W1
	await W2
	await W3
	await W4

with mp.Manager() as manager :
	_ , lists_dict = fetchLists()

	subsets = manager.list([])
	unused = manager.dict({key: value for key, value in lists_dict.items()})

	for i in [1, 2] :
		print('-----------------', i)
		start = time.time()
		asyncio.run(main(unused, subsets, i))
		end = time.time()
		print('time = ', end-start)

	for s in subsets :
		print(len(list(s.keys())), end=' ')
	with open("results/testRunParts3.txt", "w+") as f :
		for s in subsets :
			f.write("\n")
			for l, rules in s.items() :
				f.write("{0} : {1} - {2}\n".format(l, rules, "True" if len(rules) < len(lists_dict.values()) else "False"))

	for i in range(4) :
		GenQ.put('close')
	ResQ.put('close')