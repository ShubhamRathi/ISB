import os, shutil
Pairs = os.listdir("../Pairs")
count=1

for p in Pairs:
	path="../Pairs/"+str(p)+"/"
	dirs = os.listdir( path )
	for file in dirs:
		if file.endswith(".txt"):
			shutil.move(path+str(file),path+"Acq/")


