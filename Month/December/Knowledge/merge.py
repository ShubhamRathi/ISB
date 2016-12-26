import pandas as pd
targets = pd.read_csv('816_assign_patent_expand_final.csv')
acq=pd.read_csv('Acquirer_Assignees_Patent_Expand_Final.csv')

data3 = pd.concat([targets, acq])
data4 = pd.concat([targets, acq]).drop_duplicates()

data4.to_csv('finalmerged.csv')

# print data3.shape[0] - data4.shape[0]