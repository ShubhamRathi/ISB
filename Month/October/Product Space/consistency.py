import os

acq=[]
for file in os.listdir("Acquirer Density Files"):
    if file.endswith(".txt"):
    	tr=file.split('_')[0]
        acq.append(tr)

tar=[]
for file in os.listdir("Target Density Files"):
    if file.endswith(".txt"):
    	tr=file.split('_')[0]
        tar.append(tr)

ans = set(acq).intersection(set(tar))

print ans