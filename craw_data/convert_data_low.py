import pandas as pd
df = pd.read_csv('./data/raw/btc.csv')
for i in range(len(df)-1):
  df.at[i,'low'] =df.iloc[i+1]['low']

df.at[len(df)-1,'low']=0
df.drop(df.tail(1).index,inplace=True)
df.to_csv('./data/clean/btc_low.csv')