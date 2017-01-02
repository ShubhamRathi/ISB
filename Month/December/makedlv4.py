import pandas as pd
import csv
import re
import itertools, os

def cstrength(a):
	join = pd.read_csv('x.csv')
	num = list(join[(join['gvkey']==a[0]) & (join['gvkey_final']==a[1])]['patent_y'])
	num = list(set(num))
	n = len(num)
	return float(n)

def writetodl(gvkey, year, index, fold):
	info = pd.read_csv('output.csv')
	connections=info[(info['gvkey']==gvkey) & (info['year']==year)]['comps']
	connections=list(connections)
	if len(connections) >0:
		comp=[]
		try:
			comp= connections[0].strip("[]").split(",").remove('')
		except:
			comp= connections[0].strip("[]").split(",")
		comp=[x.strip() for x in comp]
		comp=[int(float(x)) for x in comp]
		comp.append(gvkey)
		comp=list(set(comp))
		# print str(gvkey)+"-"+str(len(comp))
		# os.makedirs('./Density/{}/{}/'.format(index, fold))
		# with open('./Density/{}/{}/{}.txt'.format(index, fold ,gvkey), 'a+') as output:
		# 	output.write("DL n=%d\n"%(len(comp)))
		# 	output.write("Format=edgelist1\n")
		# 	output.write("Labels embedded\n")
		# 	output.write("Data:\n")
			# perms= list(itertools.combinations(comp, 2))
			# for p in perms:
			# 	num=cstrength((p[0], p[1]))
			# 	if info[(info['gvkey']==p[0]) & (info['year']==year)].empty:
			# 		den=0
			# 	else:
			# 		den = int(info[(info['gvkey']==p[0]) & (info['year']==year)]['den'])
			# 	if den == 0:
			# 		val = float(num/1)
			# 	else:
			# 		val = float(num/den)
			# 	print p[0],p[1],val
			# 	output.write("%d %d %.10f\n"%(p[0],p[1],val)) #a,b
			# 	# -------------------------------------------------------
			# 	num=cstrength((p[1], p[0]))
			# 	if info[(info['gvkey']==p[1]) & (info['year']==year)].empty:
			# 		den = 0
			# 	else:
			# 		den = int(info[(info['gvkey']==p[1]) & (info['year']==year)]['den'])
			# 	if den == 0:
			# 		val = float(num/1)
			# 	else:
			# 		val = float(num/den)
			# 	print p[1],p[0],val
			# 	output.write("%d %d %.10f\n"%(p[1],p[0],val)) # b,a
		return 1
	return 0

def driver():
	master = pd.read_csv('Master.csv')
	count=0
	li=[]
	for index, row in master.iterrows():
		if index > 2414:
			# print index
			acq=int(row['gvkey_a'])
			targ=int(row['gvkey_t'])
			year=str(row['edate']).strip() 
			year=int(re.split(r'[-/]',year)[2])
			a=writetodl(acq, year, index, "Acq")
			t=writetodl(targ, year, index, "Target")
			if (a ==1 & t == 1):
				li.append([acq, year])
				li.append([targ, year])
				# print acq, targ
				# print "Processed "+str(count)
				count=count+1
	# print "Final count: " + str(count)
	with open("out.csv", "wb") as f:
		writer = csv.writer(f)
		writer.writerows(li)

driver()

