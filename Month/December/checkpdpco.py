import pandas as pd
import numpy as np

master = pd.read_csv('Master.csv')
pdpco = pd.read_csv('pdpcohrd.csv')

for index, row in master.iterrows():
	print index
	for serial, entry in pdpco.iterrows():
		if str(row['gvkey_a']).strip() == str(entry['gvkey']).strip():
			if int(entry['pdpco']) != int(entry['gvkey']):
				print entry['gvkey'], entry['pdpco']
