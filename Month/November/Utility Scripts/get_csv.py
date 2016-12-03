import commands as cmd
import os
for x in os.listdir("V2"):
    a = ["0"]*3
    yo = cmd.getstatusoutput("cat V2/"+x+"/CONCOR/Concor.txt | grep 'squared =' | cut -d' ' -f 3")
    a[2] = yo[1]
    for i in os.listdir("V2/"+x+"/Acq/"):
        if i.endswith("ps.txt"):
            a[0] = i.split(".")[0]
    for j in os.listdir("V2/"+x+"/Target/"):
        if j.endswith("ps.txt"):
            a[1] = j.split(".")[0]
    print ",".join(a)




