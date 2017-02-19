import pandas as pd
import numpy as np
import os

back = pd.read_csv('../IBM_Backward_Citations_expanded.csv')
ibm = pd.read_excel('../IBM.xlsx')
# fwd = pd.read_csv('../IBM_Forward_Citations_Expanded.csv')
ibm = ibm[['Patent', 'AppYearStr', 'Unique_Inventor_Number']] # Keeping relevant columns only

def Internal(data):
	row = data['Unique_Inventor_Number'].tolist()
	column = data['AppYearStr'].tolist()
	rowmin = min(row)
	rowmax = max(row)
	cmax = max(column)
	cmin = min(column)
	row = range(rowmin, rowmax+1)
	column = range(cmin, cmax+1)
	d = pd.DataFrame(np.zeros((len(row), len(column))), columns=column, index=row) # Setup 0 matrix
	ans = pd.merge(ibm, data, how='left', left_on=['Patent', 'AppYearStr'], right_on=['Citation', 'AppYearStr']) # Left join
	ans = ans.dropna()
	ans.groupby(['Unique_Inventor_Number_y', 'AppYearStr']).Citation.nunique().to_csv('temp.csv')
	temp = pd.read_csv('temp.csv', header=None)
	for index, row in temp.iterrows(): # Arrange result in matrix
		d.set_value(row[0], row[1], row[2])
	d.to_csv('Internal.csv')
	os.remove('temp.csv')

def selfcitations(data):
	row = data['Unique_Inventor_Number'].tolist()
	column = data['AppYearStr'].tolist()
	rowmin = min(row)
	rowmax = max(row)
	cmax = max(column)
	cmin = min(column)
	row = range(rowmin, rowmax+1)
	column = range(cmin, cmax+1)
	d = pd.DataFrame(np.zeros((len(row), len(column))), columns=column, index=row) # Setup 0 matrix
	ans = pd.merge(ibm, data, how='left', left_on=['Patent', 'AppYearStr', 'Unique_Inventor_Number'], right_on=['Citation', 'AppYearStr', 'Unique_Inventor_Number']) # Left join
	ans = ans.dropna()
	ans.groupby(['Unique_Inventor_Number', 'AppYearStr']).Citation.nunique().to_csv('temp.csv')
	temp = pd.read_csv('temp.csv', header=None)
	for index, row in temp.iterrows(): # Arrange result in matrix
		d.set_value(row[0], row[1], row[2])
	d.to_csv('Self.csv')
	os.remove('temp.csv')

selfcitations(back)
Internal(back)
