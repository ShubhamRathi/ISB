import pandas as pd
import re
from collections import defaultdict
import time

tnic=pd.read_csv('tnic_all years_data.csv')
master = pd.read_csv('Master2cols.csv')

scores=defaultdict(list)
for serial,entry in master.iterrows():
	start_time = time.time()
	for index, row in tnic.iterrows():
		date= str(entry['edate']).strip()
		year=re.split(r'[-/]',date)[2]
		# print int(row['gvkey_1']), int(entry['gvkey_a'])
		if int(row['gvkey_1'])==int(entry['gvkey_a']) and int(row['gvkey_2'])==int(entry['gvkey_t']):
			scores[str(row['gvkey_1'])+'_'+str(row['gvkey_2'])].append([row['eyear'],row['score']])
			# print scores[str(row['gvkey_1'])+'_'+str(row['gvkey_2'])]
	elapsed_time = time.time() - start_time
	print "Took "+str(elapsed_time)+" for 1 Master row"

print scores