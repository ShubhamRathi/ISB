import pandas as pd
import re

master = pd.read_csv('MasterFinal.csv')
Acq = pd.read_csv('CSV/AcqD.csv')
Target = pd.read_csv('CSV/TargetDensity.csv')

for index, row in master.iterrows(): # Writing Acq densities
	date= str(row['edate']).strip()
	year=re.split(r'[-/]',date)[2]
	year=int(year)
	for serial, entry in Acq.iterrows():
		if int(row['gvkey_a'])==int(entry['gvkey_a']) and int(entry['year'])==year:
			master.loc[index, 'UCI Acq Density']=entry['density']
			break;

for index, row in master.iterrows(): # Writing Target densities
	for serial, entry in Target.iterrows():
		if int(row['gvkey_t'])==int(entry['gvkey_t']):
			master.loc[index, 'UCI Target Density']=entry['density']
			break;

master.to_csv("./MasterUltimateFinal.csv", sep=',')