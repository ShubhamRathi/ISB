import os
import add
for x in os.listdir("Pairs"):
    if not ('A.csv' in os.listdir("Pairs/"+x+"/Acq/")):
        print "A:"+x
for x in os.listdir("Pairs"):
    if not ('TR.csv' in os.listdir("Pairs/"+x+"/Target/")):
        print "T:"+x
