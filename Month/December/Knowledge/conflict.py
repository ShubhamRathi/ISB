import pandas as pd
# pdpcohdr = pd.read_csv('pdpcohrd.csv')
# acq = pd.read_csv('Acquirer_Assignees.csv')

# ans = pd.merge(pdpcohdr, acq,left_on='gvkey', right_on='gvkey_a', how='right')

# ans.to_csv('pdpconflict.csv')

acq = pd.read_csv('pdpconflict.csv')

for index, row in acq.iterrows():
	if row['pdpco'] != row['gvkey']:
		print row['gvkey']

# 11040.0
# 101076.0
