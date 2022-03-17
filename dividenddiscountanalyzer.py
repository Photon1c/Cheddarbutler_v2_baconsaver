#get dividend information from a list of stocks
import pandas as pd
import yfinance as yf



#start from a list of stocks

start_list = pd.read_csv(r'test.csv')
#Create Symbols From Dataset
Symbols = start_list['symbol'].tolist()


r = .02


def screener():
    
    symm = []
    dif = []
    dividend_df = pd.DataFrame()
    for i in Symbols:
        i = i.strip()
        stock = yf.Ticker(i)
        dividends = stock.dividends
        try:
            last_dividend = dividends.iloc[-1]
            data = stock.history()
            fair_stockprice = last_dividend//r
            curr_price = (data.tail(1)['Close'].iloc[0])
            format_price = "{:.2f}".format(curr_price)
            difference = float(format_price) - float(fair_stockprice)
            format_diff = "{:.2f}".format(difference)
            print(" Stock's ", i, "last dividend is: ", 
                  last_dividend, "\n", "The fair stock price is: ", 
                  fair_stockprice, "USD per share.", "\n", "Current stock price is: ", 
                  format_price, "USD,","\n")
            print("The difference is: ", format_diff, "for stock ", i, "\n\n")        
            dif.append(format_diff)
            symm.append(stock.ticker)
        except:
            print("No dividend for stock", i)
    dividend_df["Symbol"] = symm
    dividend_df["Difference"] = dif
    print(dividend_df)
    dividend_df.to_csv("dividends.csv")
    
screener()

