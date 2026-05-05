# Quantitative Portfolio Risk Analysis using VaR, Sharpe Ratio and Rolling Metrics

Built a Python-based portfolio risk analysis tool to evaluate performance using Historical Value at Risk (VaR), Sharpe ratio, drawdown, and rolling metrics, providing insights into risk, return, and stability over time.

---

Objective

To analyze portfolio performance and quantify risk using statistical and financial metrics, helping understand downside exposure and risk-adjusted returns.

---

Methodology

- Data Source: Yahoo Finance (via yfinance)
- Returns Calculation: Daily percentage change
- Portfolio Construction: Weighted portfolio (normalized weights)

---

Metrics Used

- Historical Value at Risk (VaR - 95%)
  Estimates the 5% worst expected daily loss using historical return distribution (no normality assumption)

- Sharpe Ratio
  Measures risk-adjusted returns

- Maximum Drawdown
  Captures largest peak-to-trough decline

- Volatility
  Standard deviation of returns

- Rolling Volatility (7-day)
  Measures time-varying risk

- Rolling Sharpe Ratio (7-day)
  Tracks time-varying performance stability

---

Key Insights

- Identifies periods of high and low volatility
- Highlights instability through rolling Sharpe fluctuations
- Captures downside risk using Historical VaR and drawdown
- Evaluates diversification through correlation matrix

---

Tech Stack

- Python
- Pandas
- Matplotlib
- yfinance

---

How to Run

pip install pandas matplotlib yfinance
python portfolio_analysis.py

---

Example Output

- Portfolio returns visualization
- Drawdown curve
- Rolling volatility and Sharpe ratio plots
- Risk summary with insights

---

Project Highlights

- Modular Python functions for reusable risk analysis
- Combines static and rolling metrics for deeper insights
- Uses Historical VaR to capture real-world tail risk without distributional assumptions

---

Author

V Vishal Gowda
