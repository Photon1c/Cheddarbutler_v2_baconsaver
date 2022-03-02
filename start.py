import yfinance as yf
import pandas as pd
import numpy as np
from ticker_collector import df_final2

#start from a list of stocks, can be autogenerated by another function
import yfinance as yf
import pandas as pd
import numpy as np

#start from a list of stocks, can be autogenerated by another function
#here we import from ticker_collector.py
#start_list = pd.read_csv('testfile.csv')
#Create Symbols From Dataset
Symbols = df_final2.tolist()
target_symbols_long =[]
target_symbols_short = []


def start_screen():
    for i in Symbols:

        stock = yf.Ticker(i)
        # get stock info
        #print(stock.info['longBusinessSummary'])
        # get historical market data
        hist = stock.history(period="1mo")
        histd = pd.DataFrame(hist)
        df = pd.DataFrame()
        df["Date"] = pd.to_datetime(histd.index, unit='ms')
        df["Close"] = histd["Close"].values
        df["Volume"] = hist['Volume'].values
        df["EMA9"] = df["Close"].ewm(span=9).mean()
        df["Symbol"] = stock.ticker
        bool_long = df["EMA9"].iloc[-1] < hist["Close"].iloc[-1]  ##create Boolean to filter out stocks to go long on.
        if bool_long == True:
            target_list_long = df['Symbol'][0]
            target_symbols_long.append(target_list_long)
            print("Stock ", i, "is within buying parameters. Dataframe: " , "\n")
            print(df.tail(1))
            print("\n")
            try:
                optc = stock.option_chain("2022-02-25")
                optcl = optc.calls
                optcd = pd.DataFrame(optcl)
                optcd.rename(columns = {'lastTradeDate':'lstTrade', 'lastPrice': 'last', 'openInterest': 'oInterest', 'impliedVolatility': 'iVol'}, inplace=True)
                print("Calls for ", i, "are: ", "\n", optcd[['lstTrade', 'strike', 'last', 'bid', 'ask', 'volume', 'oInterest', 'iVol']][3:5])
            except ValueError as err:
                print("no calls available for ", i)
                print("\n")
            print(df.tail(1))
            print("\n")
        else:
            print("Stock", i, "is not within buying parameters")

        bool_short = df["EMA9"].iloc[-1] > hist["Close"].iloc[-1]  ##create second boolean to filter out stocks to short.
        if bool_short == True:
            target_list_short = df['Symbol'][0]
            target_symbols_short.append(target_list_short)
            try:
                optp = stock.option_chain("2022-02-25")
                optpl = optp.puts
                optpd = pd.DataFrame(optpl)
                optpd.rename(columns = {'lastTradeDate':'lstTrade', 'lastPrice': 'last', 'openInterest': 'oInterest', 'impliedVolatility': 'iVol'}, inplace=True)
                print("Puts for ", i, "are: ", "\n", optpd[['lstTrade', 'strike', 'last', 'bid', 'ask', 'volume', 'oInterest', 'iVol']][3:5])
            except ValueError as err:
                print("No puts available for ", i)
                print("\n")
            print("Stock ", i, "is within selling parameters. Dataframe: " , "\n")
            print(df.tail(1))
            print("\n")
        else:
            print("Stock", i, "is not within selling parameters")
 
    
    


if __name__ == '__main__':
    try:
        start_screen()
    except:
        start_screen()

print("The stocks to go long on are: ", target_symbols_long, "\n")
print("The stocks to go short on are: ", target_symbols_short)



start_list = pd.read_csv(r'path-to-your-csv-file')
#Create Symbols From Dataset
Symbols = start_list['symbol'].tolist()
target_symbols_long =[]
target_symbols_short = []


def buy_s():
    for i in Symbols:

        stock = yf.Ticker(i)
        # get stock info
        #print(stock.info['longBusinessSummary'])
        # get historical market data
        hist = stock.history(period="1mo")
        histd = pd.DataFrame(hist)
        df = pd.DataFrame()
        df["Date"] = pd.to_datetime(histd.index, unit='ms')
        df["Close"] = histd["Close"].values
        df["Volume"] = hist['Volume'].values
        df["EMA9"] = df["Close"].ewm(span=9).mean()
        df["Symbol"] = stock.ticker
        bool_long = df["EMA9"].iloc[-1] < hist["Close"].iloc[-1]  ##create Boolean to filter out stocks to go long on.
        if bool_long == True:
            target_list_long = df['Symbol'][0]
            target_symbols_long.append(target_list_long)
            print("Stock ", i, "is within buying parameters. Dataframe: " , "\n")
            print(df.tail(1))
            try:
                optc = stock.option_chain("2022-02-25")
                optc.calls
                print(optc.calls[['strike', 'lastPrice', 'bid', 'ask', 'volume', 'openInterest', 'impliedVolatility']][3:5])
            except ValueError as err:
                print("no calls available for ", i)

            print(df.tail(1))
        else:
            print("Stock", i, "is not within buying parameters")

        bool_short = df["EMA9"].iloc[-1] > hist["Close"].iloc[-1]  ##create second boolean to filter out stocks to short.
        if bool_short == True:
            target_list_short = df['Symbol'][0]
            target_symbols_short.append(target_list_short)
            try:
                optp = stock.option_chain("2022-02-25")
                optp.puts
                print(optp.puts[['lastTradeDate', 'strike', 'lastPrice', 'bid', 'ask', 'volume', 'openInterest', 'impliedVolatility']][3:5])
            except ValueError as err:
                print("no puts available for ", i)
            print("Stock ", i, "is within selling parameters. Dataframe: " , "\n")
            print(df.tail(1))
        else:
            print("Stock", i, "is not within selling parameters")
 
    
    


if __name__ == '__main__':
    try:
        buy_s()
    except:
        buy_s()

print("The stocks to go long on are: ", target_symbols_long, "\n")
print("The stocks to go short on are: ", target_symbols_short)
