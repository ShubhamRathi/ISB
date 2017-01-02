import pandas as pd
import csv

joined = pd.read_csv('x.csv')
target = pd.read_csv('816_assign_patent_expand.csv')
acq = pd.read_csv('Acquirer_Assignees.csv')
merged=[]
for index, row in target.iterrows():
	merged.append((int(row['gvkey']), int(row['deal year'])))

for index, row in acq.iterrows():
	merged.append((int(row['gvkey']), int(row['deal year'])))

merged=list(set(merged))

file=[]
count=0
for row in merged:
	comp=[]
	pats=[]
	gvkey=row[0]
	year=int(row[1])
	# print list(joined[(joined.gvkey_x==gvkey) & (joined.year_y >= year-3) & (joined.year_y <= year)]['gvkey_y'])
	# print gvkey, year
	comp=list(joined[(joined.gvkey==gvkey) & (joined.gyear >= year-3) & (joined.gyear <= year)]['gvkey_final'])
	pats=list(joined[(joined.gvkey==gvkey) & (joined.gyear >= year-3) & (joined.gyear <= year)]['patent_y'])
	# comp.append(gvkey)
	comp=list(set(comp))
	pats=list(set(pats))
	entry=[gvkey, year, len(pats), sorted(comp)]
	if entry not in file and comp != [] and comp != [gvkey]:
		print "Written 1 to file"
		count=count+1
		file.append(entry)

with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(file)


# Info = pd.read_csv('Info.csv')
# Info.drop_duplicates('gvkey').to_csv('Infov2.csv')