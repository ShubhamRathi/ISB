import pandas as pd
# citation = pd.read_csv('cite76_06.csv')
file = pd.read_csv('816_assign_patent_expand_final.csv')
join=pd.read_csv('join-left.csv')
# ans = pd.merge(citation,file,left_on='cited', right_on='patents', how='right')

ans = pd.merge(join, file,left_on='citing', right_on='patents', how='left')
ans.drop('deal year', axis=1, inplace=True)
ans.to_csv('join-final.csv')
