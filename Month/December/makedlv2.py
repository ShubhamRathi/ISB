import itertools
import pandas as pd

def cstrength(a):
	join = pd.read_csv('joinfinal.csv')
	num = list(join[(join['gvkey_x']==a[0]) & (join['gvkey_y']==a[1])]['cited_y'])
	num = list(set(num))
	n = len(num)
	return float(n)


info = pd.read_csv('v2.csv')
count=0
for index, row in info.iterrows():
	if index > -1:
		print "Serial: "+str(index)
		try:
			comp= row['connections'].strip("[]").split(",").remove('')
		except:
			comp= row['connections'].strip("[]").split(",")
		if comp != None:
			# comp= row['connections'].strip("[]").split(",")
			gvkey=int(row['gvkey'])
			comp=[int(x) for x in comp]
			print "__________________________________________"+str(gvkey)+"__________________________________________________________"
			# comp=[int(x) for x in comp]
			with open('Density Files New/{}.txt'.format(gvkey), 'a+') as output:
				if gvkey in comp:
					leng= len(comp)-1
				else:
					leng= len(comp)
				output.write("DL n=%d\n"%(leng))
				output.write("Format=edgelist1\n")
				output.write("Labels embedded\n")
				output.write("Data:\n")
				perms= list(itertools.combinations(comp, 2))
				# print perms
				for p in perms:
					num=cstrength((p[0], p[1]))
					den = int(info[info['gvkey']==p[0]]['den'])
					if den == 0:
						val = float(num/1)
					else:
						val = float(num/den)
					# print num, den
					# print val
					output.write("%d %d %.10f\n"%(p[0],p[1],val)) #a,b
					num=cstrength((p[1], p[0]))
					den = int(info[info['gvkey']==p[1]]['den'])
					if den == 0:
						val = float(num/1)
					else:
						val = float(num/den)
					# print num, den
					# print val
					output.write("%d %d %.10f\n"%(p[1],p[0],val)) # b,a
			count=count+1
			print "Written "+str(count) + " genuine files"
		else:
			continue
