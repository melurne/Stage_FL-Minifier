from itertools import combinations
import multiprocessing as mp
import asyncio
from threading import Thread
from queue import Queue
import itertools
import time
import asyncio_pipe

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

def worker(GenQ, ResQ) :
	_ , lists_dict = fetchLists()
	# connection = asyncio_pipe.Connection(GenQ)
	while True :
		# print('recieving')
		part = GenQ.get()
		# print('recieved')


		if part == 'close' :
			# print('worker exitting')
			ResQ.put('close')
			return


		if validateSubset(lists_dict, part) :
			ResQ.put_nowait(part)

async def Producer(GenQ, unused, n, ResQ) :
	i = 0
	lists = {key: value for key, value in unused.items()}
	for part in generateParts(lists, n) :
		print(i, end='\r')
		i+=1
		GenQ.put(part)
	time.sleep(1)
	for _ in range(3) :
		GenQ.put('close')
		# ResQ.put('close')
		# print('sending close call')
	return

async def updator(ResQ, unused, subsets) :
	while True :
		part = ResQ.get()
		if part == 'close' :
			return
		for l in part.keys():
			if l in unused :
				del[unused[l]]
		if len(part) > 0 :
			subsets.append(part)

async def main(unused, subsets, i) :
	GenQ = mp.Queue(500)
	ResQ = mp.Queue(500)
	# GenR, GenW = mp.Pipe(duplex=False)

	# it1, it2 = itertools.tee(generateParts(unused, i), 2)
	# print(type(it1))
	# prod1 = asyncio.create_task(producerTee(GenQ1, it1))
	# prod2 = asyncio.create_task(producerTee(GenQ2, it2))
	prod = asyncio.create_task(Producer(GenQ, unused, i, ResQ))
	upda = asyncio.create_task(updator(ResQ, unused, subsets))

	W1 = mp.Process(target=worker, args=(GenQ, ResQ))
	W2 = mp.Process(target=worker, args=(GenQ, ResQ))
	W3 = mp.Process(target=worker, args=(GenQ, ResQ))
	# W4 = mp.Process(worker, (GenQ, ResQ))
	W1.start()
	W2.start()
	W3.start()
	await prod
	# print('prod exited')
	# W1.terminate()
	# W2.terminate()
	# W3.terminate()
	# await prod1
	# await prod2
	await upda
	# print('update')

	# W4.start()

	W1.join()
	W2.join()
	W3.join()
	# W4.join()



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

	subsets.append(unused)
	for s in subsets :
		print(len(list(s.keys())), end=' ')
	with open("testRunParts3.txt", "w+") as f :
		for s in subsets :
			f.write("\n")
			for l, rules in s.items() :
				f.write("{0} : {1} - {2}\n".format(l, rules, "True" if len(rules) < len(lists_dict[l]) else "False"))