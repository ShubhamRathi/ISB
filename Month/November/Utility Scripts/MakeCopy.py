import os, shutil
Pairs = os.listdir("../Pairs")

for p in Pairs:
	path="../Pairs/"+str(p)+"/Target/"
	dirs = os.listdir( path )
	for file in dirs:
		if file.endswith(".txt"):
			os.system('cp '+path+str(file)+" "+path+"T.txt")
