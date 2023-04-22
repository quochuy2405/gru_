import pandas as pd
from yahoofinancials import YahooFinancials
yahoo_financials = YahooFinancials('BTC-USD')
data = yahoo_financials.get_historical_price_data(start_date='2009-01-01', 
                                                  end_date='2022-12-31', 
                                                  time_interval='daily')
btc_df = pd.DataFrame(data['BTC-USD']['prices'])
#btc_df.rename(columns={'formatted_date': 'Date'},inplace = True)
btc_df = btc_df.drop('date', axis=1).set_index('formatted_date')
btc_df.to_csv('./data/raw/btc.csv',encoding='utf8')