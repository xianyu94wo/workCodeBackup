import pandas as pd
fo1 = open(r"I:\2018pre\cimissdataprocess\2018_pre_test\527371.csv")
#df1 = pd.read_csv(fo1, index_col=['Date', 'Time'])
df1 = pd.read_csv(fo1)
print(df1)
df2= df1.drop_duplicates(['Date', 'Time'])
print(df2)

'''
fo2 = open(r"I:\\2018pre\\cimissdataprocess\\base.csv")
df2 = pd.read_csv(fo2, index_col=['Date', 'Time'])
print(df1)
'''
#newDf = pd.concat([df2,df1],axis=1)