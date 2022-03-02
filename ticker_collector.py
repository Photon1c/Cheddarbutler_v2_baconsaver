import pandas as pd



#can get from any website displaying daily active stock tickers, html layout determines how data frame is constructed.
#could also import df_final2 into start.py for automatic retrieval
df = pd.read_html("https://www.marketwatch.com/tools/screener/after-hours")
dfg = df[0]
#create new series that keeps only first string value in 'Symbol Symbol' column, discarding anything after space
dfgainers = dfg['Symbol  Symbol'].str[:4]
dflosers = df[1]
dflosers2 = dflosers['Symbol  Symbol'].str[:4]
dfgainers2 = dfgainers
df_final = dfgainers2.append(dflosers2)
df_final2 = pd.DataFrame()
df_final2["Symbol"] = df_final
df_final2["Symbol"].to_csv(r'[path to your csv file with stock tickers]')


#test to see if full dataframe can be extracted by printing main frame
#print(dfg, dgl) 
#test final list
print(df_final2)
