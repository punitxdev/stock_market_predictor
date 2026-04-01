<div align="center">

# 📈 Stock Market Predictor

### _AI-powered stock price forecasting with Linear Regression_

<br>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Yahoo Finance](https://img.shields.io/badge/yfinance-720E9E?style=for-the-badge&logo=yahoo&logoColor=white)](https://pypi.org/project/yfinance/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)

<br>

A full-stack web app that fetches real-time stock data via **Yahoo Finance**, trains a **Linear Regression** model, and forecasts prices up to **30 days** into the future — complete with a dynamic dark-mode glassmorphism UI and matplotlib forecast graphs.

<br>

---

</div>

<br>

## 🎯 What It Does

<table>
<tr>
<td width="50%">

### 🤖 AI Prediction Engine

- **Linear Regression** trained on historical Close prices
- Fetches live data from **Yahoo Finance** (`yfinance`)
- Forecasts **1–30 business days** ahead
- **Smart caching** — trains once, saves as `.pkl`, reuses instantly
- Auto-generates a **matplotlib forecast graph** (dark-themed)

</td>
<td width="50%">

### 🎨 Premium Interface

- 🌑 **Dark glassmorphism** — frosted glass cards with animated blobs
- 🎨 **Gradient text** — animated purple-to-green heading
- 📊 **Side-by-side layout** — input form + results panel
- 📈 **Trend indicators** — green ↗ for gains, red ↘ for drops
- ⏳ **Smart loading states** — "Loading model..." vs "Predicting..."

</td>
</tr>
</table>

<br>

## ✨ Key Features

- 🔄 **Any Stock Ticker** — Works with any valid Yahoo Finance symbol (AAPL, TSLA, GOOGL, NVDA, AMZN...)
- 📉 **Forecast Graph** — Auto-generated matplotlib chart showing historical prices + predicted trajectory
- 💾 **Model Caching** — Trained models saved as `.pkl` files for instant re-predictions
- 🧮 **Day-by-Day Forecast** — Individual predictions with price deltas and trend direction
- 🌐 **Auto-Opens Browser** — Flask server launches your browser automatically on startup
- 📱 **Responsive** — Stacks cleanly on mobile devices

<br>

## 🚀 Quick Start

```bash
# Clone it
git clone https://github.com/punitxdev/stock_market_predictor.git
cd stock_market_predictor

# Install dependencies
pip install flask pandas numpy scikit-learn yfinance joblib matplotlib

# Run it
python3 stock_prediction.py
```

> App auto-opens at **http://127.0.0.1:5005** — enter a ticker, set forecast days, and hit predict!

<br>

## 🔮 How It Works

```
1. Enter stock ticker (e.g. AAPL) + number of future days (1–30)
2. Backend checks for cached .pkl model for that ticker
3. If no cache → fetches data from Yahoo Finance → trains LinearRegression → saves .pkl
4. Model predicts future close prices based on historical patterns
5. Generates a dark-themed matplotlib graph (historical + predicted)
6. Returns predictions with trend arrows (↗ gain / ↘ drop) per day
```

<br>

## 📁 Project Structure

```
📦 stock_market_predictor
 ┣ 🐍 stock_prediction.py     → Flask server + Linear Regression model + graph generation
 ┣ 📄 index.html              → Full frontend UI (glassmorphism, inline CSS & JS)
 ┣ 📂 static/
 ┃   ┗ 📊 {TICKER}_graph.png  → Auto-generated forecast charts
 ┣ 🤖 {TICKER}_prediction.pkl → Cached trained models per stock
 ┗ 📝 README.md
```

<br>

## 🛠️ Built With

| Tech | Purpose |
|---|---|
| **Python** | Backend language |
| **Flask** | Web server & API endpoints |
| **scikit-learn** | Linear Regression model |
| **yfinance** | Real-time stock data from Yahoo Finance |
| **Pandas / NumPy** | Data manipulation |
| **Matplotlib** | Forecast graph generation |
| **joblib** | Model serialization & caching |
| **HTML5 / CSS3 / JS** | Glassmorphism frontend UI |

<br>

## ⚠️ Disclaimer

> This is a **machine learning demo for educational purposes only**. Stock predictions are inherently uncertain. **Do not** use this tool for actual financial decisions. Always consult a qualified financial advisor.

<br>

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

```bash
# Fork → Branch → Commit → Push → PR
git checkout -b feature/lstm-model
git commit -m "Add LSTM prediction model"
git push origin feature/lstm-model
```

<br>

## 📄 License

Open source under the [MIT License](LICENSE).

<br>

<div align="center">

---

**Made with ❤️ by [punitxdev](https://github.com/punitxdev)**

_If you found this useful, give it a ⭐!_

</div>
