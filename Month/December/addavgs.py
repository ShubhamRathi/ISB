import pandas as pd
import re

master = pd.read_csv('Master.csv')

count=0;
notfound=[]
for index, row in master.iterrows():
	print index
	date= str(row['edate']).strip()
	year=re.split(r'[-/]',date)[2]
	year=int(year)
	try:
		CSV= pd.read_csv('1/'+str(row['gvkey_a'])+'.csv')
	except:
		notfound.append(str(row['gvkey_a']))
		master.loc[index, 'TNIC 3 years avg']='No Data'
		master.loc[index, 'TNIC > 3 years avg']='No Data'
		master.loc[index, 'threeyrs']='No Data'
		master.loc[index, 'len mthreeyrs']='No Data'
		master.loc[index, 'len threeyrs']='No Data'
		continue
	three=[]
	mthree=[]
	yth=[]
	ymth=[]
	for serial, entry in CSV.iterrows():
		if int(entry['gvkey_1'])==int(row['gvkey_a']) and int(entry['gvkey_2'])==int(row['gvkey_t']):
			yr =int(entry['eyear'])
			if year-3 <= yr <= year:
				three.append(entry['score'])
				yth.append(yr)
			else:
				mthree.append(entry['score'])
				ymth.append(yr)
	if len(three)==0:
		master.loc[index, 'TNIC 3 years avg']=0
	else:
		master.loc[index, 'TNIC 3 years avg']=float(sum(three)/len(three))
	if len(mthree)==0:
		master.loc[index, 'TNIC > 3 years avg']=0
	else:
		master.loc[index, 'TNIC > 3 years avg']=float(sum(mthree)/len(mthree))
	master.loc[index, 'threeyrs']=str(yth)
	master.loc[index, 'mthreeyrs']=str(ymth)
	master.loc[index, 'len mthreeyrs']=str(len(mthree))
	master.loc[index, 'len threeyrs']=str(len(three))
	# print "_______________________________________"
	# print row['gvkey_a'], row['gvkey_t'], row['TNIC 3 years avg'], row['TNIC > 3 years avg']

print "No match for "+str(len(notfound))
# print notfound
master.to_csv("./MasterFinal.csv", sep=',')