import pandas as pd

master = pd.read_csv('Master.csv')
results = pd.read_csv('results.csv')

i=0
# print results[results.columns[0]][0]

for index, row in master.iterrows():
	if str(row['gvkey_a']).strip() == '7257':
		print row['gvkey_a'], row['gvkey_t']