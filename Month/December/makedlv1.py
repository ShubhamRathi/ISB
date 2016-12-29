import pandas as pd
import csv

joined = pd.read_csv('joinfinal.csv')
target = pd.read_csv('816_assign_patent_expand.csv')
acq = pd.read_csv('Acquirer_Assignees.csv')

save=[]
for index, row in target.iterrows():
	comp=[]
	pats=[]
	gvkey=row['gvkey']
	year=int(row['deal year'])
	# print list(joined[(joined.gvkey_x==gvkey) & (joined.year_y >= year-3) & (joined.year_y <= year)]['gvkey_y'])
	comp=list(joined[(joined.gvkey_x==gvkey) & (joined.year_y >= year-3) & (joined.year_y <= year)]['gvkey_y'])
	pats=list(joined[(joined.gvkey_x==gvkey)]['cited_y'])
	# comp.append(gvkey)
	comp=list(set(comp))
	pats=list(set(pats))
	with open('Info.csv', 'a') as myfile:
		writer = csv.writer(myfile, dialect='excel')
		row=[gvkey, len(pats), comp]
		writer.writerow(row)

for index, row in acq.iterrows():
	comp=[]
	pats=[]
	gvkey=row['gvkey']
	year=int(row['deal year'])
	# print list(joined[(joined.gvkey_x==gvkey) & (joined.year_y >= year-3) & (joined.year_y <= year)]['gvkey_y'])
	comp=list(joined[(joined.gvkey_x==gvkey) & (joined.year_y >= year-3) & (joined.year_y <= year)]['gvkey_y'])
	pats=list(joined[(joined.gvkey_x==gvkey)]['cited_y'])
	# comp.append(gvkey)
	comp=list(set(comp))
	pats=list(set(pats))
	with open('Info.csv', 'a') as myfile:
		writer = csv.writer(myfile, dialect='excel')
		row=[gvkey, len(pats), comp]
		writer.writerow(row)


# Info = pd.read_csv('Info.csv')
# Info.drop_duplicates('gvkey').to_csv('Infov2.csv')