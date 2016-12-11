import pandas as pd
import re
import numpy as np

tnic=pd.read_csv('tnic_all years_data.csv')
master = pd.read_csv('MasterwithR.csv')
acqd = pd.read_csv('Density Files/AcqDensity.csv')
tard = pd.read_csv('Density Files/TargetDensity.csv')

acq_m=[]
for index, row in master.iterrows():
	if not np.isnan(row['R']):
		acq_m.append(row['gvkey_a'])

acq_d=[]
for index, row in acqd.iterrows():
	acq_d.append(int(row[0]))

acq_m=set(acq_m)
acq_d=set(acq_d)

print len(set.intersection(acq_d,acq_m))