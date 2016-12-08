import pandas as pd

master = pd.read_csv('Master.csv')
results = pd.read_csv('results.csv')

i=0
# print results[results.columns[0]][0]

for index, row in master.iterrows():
	for serial, entry in results.iterrows():
		# print type(entry[0].split('_')[0])
		# print str(row['gvkey_a']).strip(), entry[0].split('_')[0].strip()
		if str(row['gvkey_a']).strip() == str(entry[0].split('_')[0].strip()) and str(row['gvkey_t']).strip() == str(entry[1].split('_')[0].strip()):
			master.loc[index, 'R']=float(entry[2])
			i+=1

master.to_csv("./MasterwithR.csv", sep=',')
print str(i)+" values written to file"