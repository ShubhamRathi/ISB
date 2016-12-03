import pandas as pd
def add(arg):
    X= pd.read_csv(arg+"/Acq/A.csv", index_col=0)
    Y= pd.read_csv(arg+"/Target/TR.csv" , index_col=0)

    # print X.shape
    # print Y.shape

    all_cols = X.columns | Y.columns
    all_indices = X.index | Y.index

    Z= X.add(Y, fill_value=0).reindex(index=all_indices,columns=all_cols).fillna(0)

    print Z.shape

    #Z.to_csv(arg+"/Sum/sum.csv", sep=',')
