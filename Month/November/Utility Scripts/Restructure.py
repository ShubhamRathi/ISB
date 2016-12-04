import csv, os, shutil
Pairs = os.listdir("../Pairs")

for p in Pairs:
	p="../Pairs/"+str(p)
	os.makedirs(p+"/Acq/")
	os.makedirs(p+"/Target/")
	os.makedirs(p+"/TargetT/")
	os.makedirs(p+"/Sum/")
	os.makedirs(p+"/CONCOR/")
