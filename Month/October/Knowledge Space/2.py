import csv
from pprint import pprint

file1reader = csv.reader(open("816.csv"), delimiter=",")
file2reader = csv.reader(open("Pruned.csv"), delimiter=",")

L1 = list(file1reader)
L2 = list(file2reader)

matched=[]
pmatched=[]

for row1 in L1:
	for row2 in L2:
		for i in [2,5,8,11]:
			if row2[i]:
				if int(row1[0]) == int(row2[i]):
					if int(row2[i-1]) <= int(row1[1]) <= int(row2[i+1]):
						matched.append(row2)
					else:
						pmatched.append(row2)

print "Fully Matched: "+ str(len(matched))+" ["+ str(float(len(matched)/float(len(L1))) * 100) +"%]"
print "Parlially Matched: "+ str(len(pmatched))+" ["+ str(float(len(pmatched)/float(len(L1))) * 100) +"%]"
print "Unmatched: "+ str(len(L1)-len(matched)-len(pmatched))+" ["+ str(float((len(L1)-len(matched)-len(pmatched))/float(len(L1))) * 100) +"%]"
