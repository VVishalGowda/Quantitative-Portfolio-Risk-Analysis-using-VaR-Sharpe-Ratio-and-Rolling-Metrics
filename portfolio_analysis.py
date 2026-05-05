import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# to get data

def get_data(tickers,period="1mo"):
    portfolio_data=yf.download(tickers,period=period)["Close"]
    portfolio_df=pd.DataFrame(portfolio_data)
    return portfolio_df

# to calculate returns

def calculate_returns(portfolio_df):
    returns_df=portfolio_df.pct_change().dropna()
    return returns_df

# to calculate weighted portfolio

def portfolio_returns(returns_df,weights):
    weights=pd.Series(weights)
    weights=weights/weights.sum()
    port_returns=(returns_df*weights).sum(axis=1)
    return port_returns

# to  calculate metric

def calculate_metrics(port_returns,returns_df):
    avg_returns=port_returns.mean()
    volatility=port_returns.std()
    correlation=returns_df.corr()
    var_95=port_returns.quantile(0.05)
    cumulative_return=((1+port_returns).prod()-1)
    return avg_returns,volatility,correlation,var_95,cumulative_return

# to  calculated drawdown

def calculate_drawdown(port_returns):
    portfolio_cum = (1 + port_returns).cumprod()
    peak = portfolio_cum.cummax()
    drawdown = (portfolio_cum - peak) / peak
    max_dd = drawdown.min()
    return max_dd

#sharpe ratio

def sharpe_ratio(port_returns):
    val=port_returns.std()
    if val == 0:
        return float('nan')
    sharpe = (port_returns.mean()/val)*(252**0.5)

    return sharpe

# to get rolling volatility 

def rolling_volatility(port_returns,window=7):
    rolling_vol=port_returns.rolling(window).std()
    return rolling_vol


# to get rolling sharpe ratio

def rolling_sharpe_ratio(port_returns,window=7):
    rolling_mean = port_returns.rolling(window).mean()
    rolling_std = port_returns.rolling(window).std()
    rolling_sharpe = rolling_mean/rolling_std
    rolling_sharpe = rolling_sharpe.replace([float('inf'),float('-inf')],0)
    return rolling_sharpe


# printing summary

def print_summary(avg_return, volatility, correlation, var_95, cumulative_return, max_dd,  returns_df,sharpe,rolling_vol,rolling_sharpe):

    print("\n--- Portfolio Summary ---")
    print("Average Return:", avg_return)
    print("Volatility:", volatility)
    print("VaR (95%):", var_95)
    print("Max Drawdown:", max_dd)
    print("Cumulative Return:", cumulative_return)

    print("\n--- Correlation Matrix ---")
    print(correlation)

    print("\n--- Insights ---")

    print("Most volatile asset:", returns_df.std().idxmax())
    print("Least volatile asset:", returns_df.std().idxmin())

    print("Best performing asset:", returns_df.mean().idxmax())
    print("Sharpe ratio:", sharpe )
    print("Latest 7-day rolling volatility:", rolling_vol.iloc[-1])
    print("Latest 7-day rolling sharpe ratio:",rolling_sharpe.iloc[-1])

    #relative insights

    if volatility < 0.01:
        print("Portfolio shows low volatility → relatively stable.")
    elif volatility < 0.02:
        print("Portfolio shows moderate volatility → manageable risk.")
    else:
        print("Portfolio shows high volatility → higher risk exposure.")

    if max_dd > -0.1:
        print("Drawdown is low → limited downside risk.")
    elif max_dd > -0.3:
        print("Drawdown is moderate → acceptable risk.")
    else:
        print("Drawdown is high → significant loss potential.")

    avg_corr = correlation.mean().mean()

    if avg_corr < 0.3:
        print("Good diversification → assets are weakly correlated.")
    else:
        print("Low diversification → assets move together.")
    
    if sharpe > 1:
        print("Portfolio shows good risk adjusted returns")
    else:
        print("Portfolio can improve risk adjusted returns")
    
#visualization

def plot_growth(port_returns):
    portfolio_cum = (1 + port_returns).cumprod()
    plt.figure()
    plt.plot(portfolio_cum)
    plt.title("Portfolio Growth")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.show()

def plot_returns(port_returns):
    plt.figure()
    plt.plot(port_returns)
    plt.title("Daily Portfolio Returns")
    plt.xlabel("Date")
    plt.ylabel("Returns")
    plt.show()

def plot_drawdown(port_returns):
    portfolio_cum = (1 + port_returns).cumprod()
    peak = portfolio_cum.cummax()
    drawdown = (portfolio_cum - peak) / peak
    plt.figure()
    plt.plot(drawdown)
    plt.title("Portfolio Drawdown")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.show()

def plot_rolling_volatility(port_returns):
    rolling_vol=rolling_volatility(port_returns)

    plt.figure()
    plt.plot(rolling_vol)
    plt.title("Rolling Volatility for 7 days")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.show()

def plot_rolling_sharpe(port_returns):
    rolling_sharpe = rolling_sharpe_ratio(port_returns)
    
    plt.figure()
    plt.plot(rolling_sharpe)
    plt.title("Rolling Sharpe Ratio for 7 days")
    plt.xlabel("Date")
    plt.ylabel("Sharpe ratio")
    plt.show()


if __name__ == "__main__":
    tickers = ("RELIANCE.NS","TATASTEEL.NS","TCS.NS")

    prices = get_data(tickers)
    returns_df = calculate_returns(prices)

    weights = {
        "RELIANCE.NS": 0.35,
        "TATASTEEL.NS": 0.35,
        "TCS.NS": 0.30
    }

    port_returns = portfolio_returns(returns_df, weights)

    avg_return, volatility, correlation, var_95, cumulative_return = calculate_metrics(port_returns, returns_df)

    max_dd = calculate_drawdown(port_returns)
    sharpe= sharpe_ratio(port_returns)
    rolling_vol = rolling_volatility(port_returns)
    rolling_sharpe = rolling_sharpe_ratio(port_returns)

    print_summary(avg_return, volatility, correlation, var_95, cumulative_return, max_dd,  returns_df,sharpe,rolling_vol,rolling_sharpe)
    plot_growth(port_returns)
    plot_returns(port_returns)
    plot_drawdown(port_returns)
    plot_rolling_volatility(port_returns)
    plot_rolling_sharpe(port_returns)
   
    
