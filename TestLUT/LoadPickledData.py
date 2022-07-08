import pickle

with open("/home/maxence/StageInria/filterlistsairflow/filter_list_parser/data/statistics/shared_rules.pickle") as f:
	data = pickle.load(f, encoding='utf-8')

print(data)