import pandas as pd
import yfinance as yf




#get user preferences prior to running script
#ask user to choose whether to use a list of stocks from a csv file or to use the ticker_collector.py script to get after hours stocks from marketwatch.
print(' Welcome to Bacon Saver!', '\n\n', 'Are you using a list of ticker symbols from a csv file,', '\n', 'or would you like to get a list from the after hours screener on marketwatch?')
set_source = input(" Please enter CSV or MOV to set the source of the stock list.")
#ask user to set the EMA days
u_ema = int(input(' Enter the desired number of days to calculate the exponential moving average, 9 is the recommended value.'))

#ask user to set the option chain expiration date
user_ochain = input(' Enter the option chain expiration date in YYYY-MM-DD format.')


def display_status():
    print("The source of the stock list will be: ", set_source)              
    print("The exponential moving average will be calculated using", user_ema, "days")                
    print("The option chain expiration used will be: ", user_ochain)
    print("Please wait while the program runs. Starting script...")
    
    
movers_list =[]
movers_df = pd.DataFrame()

def get_movers():
    df = pd.read_html("https://www.marketwatch.com/tools/screener/after-hours")
    dfg = df[0]
    #create new series that keeps only first string value in 'Symbol Symbol' column, discarding anything after space
    dfgainers = dfg['Symbol  Symbol'].str[:4]
    dflosers = df[1]
    dflosers2 = dflosers['Symbol  Symbol'].str[:4]
    dfgainers2 = dfgainers.str.strip()
    df_final = dfgainers2.append(dflosers2.str.strip())
    df_final2 = pd.DataFrame()
    df_final2["Symbol"] = df_final
    df_final2.to_csv(r'PATH_TO_CSV')
    movers_list.append(df_final2["Symbol"])


#get web list saved to csv file and create new list
manual_list = pd.read_csv(r'PATH_TO_CSV')
auto_list = pd.read_csv(r'PATH_TO_CSV')
#Create Symbols From Dataset
target_symbols_long =[]
target_symbols_short = []      
movers_df = pd.DataFrame(movers_list)
short_df = []
long_df = []
master_df = pd.DataFrame()

def screener():
    for i in Symbols:
        i = i.strip()
        stock = yf.Ticker(i)
        # get stock info
        #print(stock.info['longBusinessSummary'])
        # get historical market data
        hist = stock.history(period="1mo")
        histd = pd.DataFrame(hist)
        df = pd.DataFrame()
        df["Symbol"] = str(i)
        df["Date"] = pd.to_datetime(histd.index, unit='ms')
        df["Close"] = histd["Close"].values
        df["Volume"] = hist['Volume'].values
        df["EMA9"] = df["Close"].ewm(span=u_ema).mean()
        df["Symbol"] = stock.ticker
        df.fillna("nan")
        bool_long = df["EMA9"].iloc[-1] < hist["Close"].iloc[-1]  ##create Boolean to filter out stocks to go long on.
        if bool_long == True:
            target_list_long = df['Symbol'][0]
            target_symbols_long.append(target_list_long)   
            print("Stock ", i, "is within buying parameters. Dataframe: ")
            print(df.tail(1))
            try:
                optc = stock.option_chain(user_ochain)
                optcz = optc.calls[['strike', 'lastPrice', 'bid', 'ask', 'volume', 'openInterest', 'impliedVolatility']][9:16]
                optczdf = pd.DataFrame(optcz)
                long_df.append(optczdf) 
                print("BUY ", i, ": ", "\n", optczdf)
            except ValueError as err:
                print("no calls available for ", i, "\n\n")
                           
            else:
                print("Stock", i, "is not within buying parameters", "\n\n")
        master_df.append(long_df)
        bool_short = df["EMA9"].iloc[-1] > hist["Close"].iloc[-1]  ##create second boolean to filter out stocks to short.
        if bool_short == True:
            target_list_short = df['Symbol'][0]
            target_symbols_short.append(target_list_short)
            print("Stock ", i, "is within selling parameters. Dataframe: ")
            print(df.tail(1))
            try:
                optp = stock.option_chain(user_ochain)
                optpz = optp.puts[['lastTradeDate', 'strike', 'lastPrice', 'bid', 'ask', 'volume', 'openInterest', 'impliedVolatility']][9:16]
                print("Stock ", i, "is within selling parameters. Dataframe: ")
                optpzdf = pd.DataFrame(optpz)
                short_df.append(optpzdf)
                print("SELL ", i, ": ", "\n", optpzdf, "\n\n")
            except ValueError as err:
                print("no puts available for ", i, "\n\n")    
                
            else:
                print("Stock", i, "is not within selling parameters", "\n\n\n")
        master_df.append(short_df)
    
    




    

if __name__ == '__main__':
    display_status()
    if(set_source == 'CSV'):
        Symbols = manual_list['Symbol'].tolist()
    elif(set_source == 'MOV'):
        get_movers()
        Symbols = auto_list['Symbol'].tolist()
    else:
        print("Please run script again.")
    screener()


print("The stocks to go long on are: ", target_symbols_long, "\n")
print("The stocks to go short on are: ", target_symbols_short)  
        
        