import os
import add
for x in os.listdir("Pairs"):
    if ('A.csv' in os.listdir("Pairs/"+x+"/Acq/")):
        print "Pairs"+x
        add.add("Pairs/"+x)
