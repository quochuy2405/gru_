import pandas as pd
df = pd.read_csv('./data/raw/btc.csv')
for i in range(len(df)-1):
  df.at[i,'open'] =df.iloc[i+1]['open']

df.at[len(df)-1,'open']=0
df.drop(df.tail(1).index,inplace=True)
df.to_csv('./data/clean/btc_open.csv')