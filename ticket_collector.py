import pandas as pd

df = pd.read_html("https://www.marketwatch.com/tools/screener/after-hours")
dfg = df[0]
#create new series that keeps only first string value in 'Symbol Symbol' column, discarding anything after space
dfgg = dfg['Symbol  Symbol'].str[:4]
dfl = df[1]
dfll = dfl['Symbol  Symbol'].str[:4]

print(dfgg, dfll)
#test to see if full dataframe can be extracted by printing main frame
#print(dfg, dgl) 