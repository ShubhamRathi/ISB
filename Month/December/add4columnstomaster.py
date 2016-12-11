import pandas as pd
import re

tnic=pd.read_csv('tnic_all years_data.csv')
master = pd.read_csv('MasterwithR.csv')
acqd = pd.read_csv('Density Files/AcqDensity.csv')
tard = pd.read_csv('Density Files/TargetDensity.csv')


i=0
acql=acqd['gv']
for index, row in master.iterrows(): # Adding Acq Densities
	for serial, entry in acqd.iterrows():
		date= str(row['edate']).strip()
		year=re.split(r'[-/]',date)[2]
		# print year
		# print str(row['gvkey_a']).strip(), str(entry[0]).strip()
		if str(row['gvkey_a']).strip() == str(int(entry[0])).strip() and year == str(int(entry[1])).strip():
			i+=1
			master.loc[index, 'Acq Density']=float(entry[4])
# print "Added "+str(i) +" Acq densities"
i=0
for index, row in master.iterrows(): # Adding Target Densities
	for serial, entry in tard.iterrows():
		date= str(row['edate']).strip()
		year=re.split(r'[-/]',date)[2]
		# print year
		# print str(row['gvkey_a']).strip(), str(entry[0]).strip()
		if str(row['gvkey_t']).strip() == str(int(entry[0])).strip():
			i+=1
			master.loc[index, 'Target Density']=float(entry[3])

print "Added "+str(i) +" Target densities"
i=0
master.to_csv("./Master2cols.csv", sep=',')

for index, row in master.iterrows(): # Adding Score from TNIC
	for serial, entry in tnic.iterrows():
		date= str(row['edate']).strip()
		year=re.split(r'[-/]',date)[2]
		# print year
		# print str(row['gvkey_a']).strip(), str(entry[0]).strip()
		# print str(row['gvkey_t']).strip(), str(entry['gvkey_1']).strip()		
		if str(row['gvkey_t']).strip() == str(int(entry['gvkey_1'])).strip() and str(row['gvkey_a']).strip() == str(int(entry['gvkey_2'])).strip() and str(year).strip() == str(int(entry['eyear'])).strip():
			i+=1
			master.loc[index, 'TNIC 3 years avg']=entry['score']
			print "Found & Added to Master"
print "Added "+str(i) +" TNIC scores"
i=0

# for index, row in master.iterrows(): # Adding Score from TNIC
# 	for serial, entry in tnic.iterrows():
# 		date= str(row['edate']).strip()
# 		year=re.split(r'[-/]',date)[2]
# 		# print year
# 		# print str(row['gvkey_a']).strip(), str(entry[0]).strip()
# 		if str(row['gvkey_t']).strip() == str(entry['gvkey_1']).strip() and str(row['gvkey_a']).strip() == str(entry['gvkey_2']).strip():

# 			master.loc[index, 'TNIC 3 years avg']=entry['score']

master.to_csv("./Master3cols.csv", sep=',')