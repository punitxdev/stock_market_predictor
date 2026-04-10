<div align="center">

# Stock Market Predictor

### AI-powered stock price forecasting using Linear Regression.

<br>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Yahoo Finance](https://img.shields.io/badge/yfinance-720E9E?style=for-the-badge&logo=yahoo&logoColor=white)](https://pypi.org/project/yfinance/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)

<br>

A full-stack web application that fetches real-time baseline data via **Yahoo Finance**, trains a structural **Linear Regression** model, and forecasts price arrays up to **30 days** into the future. It includes a dynamic dark-mode interface and visually rendered `matplotlib` projection graphs.

<br>

---

</div>

<br>

## Overview

<table>
<tr>
<td width="50%">

### AI Prediction Engine

- Implements **Linear Regression** constraints compiled from historical sequential close metrics.
- Maps continuous live pipeline data by pulling directly via **Yahoo Finance** (`yfinance`).
- Compiles forecasts spanning **1–30 business days** effectively.
- **Smart model caching**: Serializes optimized model via `.pkl` to guarantee fractional inference lag on repeat processing.
- Automatically calculates and binds formatted **matplotlib projection graphs**.

</td>
<td width="50%">

### Precision Interface

- **Dark layout design** combined with structured semantic frosted presentation views.
- **Gradient text configurations** to designate headers structurally.
- **Multi-panel rendering**: Dual input variable form against result-set panels.
- **Trend indicators**: Structural UI designations indicating directional movement vectors.
- **Asynchronous loading variables**: Dynamic UI state processing representations.

</td>
</tr>
</table>

<br>

## Key Features

- **Tethered Stock Input**: Parses universally recognized Yahoo Finance symbols efficiently (AAPL, TSLA, GOOGL, NVDA, etc).
- **Forecast Graph Generator**: Procedural historical timeline graphs overlaying modeled predictive values.
- **Instant Result Serializing**: `joblib` integrated caching configurations limiting iterative server lag on repeated models.
- **Daily Trend Forecasting**: Calculated incremental shifts identifying short-duration vector mappings over the targeted temporal scope.
- **Self-Initializing Instance**: The Flask logic naturally bootstraps system routing natively post-launch.

<br>

## Quick Start

```bash
# Clone the root repository package
git clone https://github.com/punitxdev/stock_market_predictor.git
cd stock_market_predictor

# Define core pipeline prerequisites
pip install flask pandas numpy scikit-learn yfinance joblib matplotlib

# Execute backend structural initialization
python3 stock_prediction.py
```

> The configured server executes operations via **http://127.0.0.1:5005**. Establish target ticker mapping factors to initialize execution.

<br>

## How It Works

```text
1. Define designated target array constraints (e.g. AAPL) combined with targeted sequential forecasting period spanning 1–30 parameters.
2. Caching matrix scans server volumes mapping corresponding existing `.pkl` arrays.
3. Upon Cache Miss → Core routine targets `yfinance` to parse index data → Computes variable `LinearRegression` → Serializes cache representation logic.
4. Output arrays analyze input historical points forming mapped predictions.
5. Dynamic rendering structure creates an equivalent plotting frame via `matplotlib`.
6. Outputs return generated predictions merged with normalized sequential vector structures.
```

<br>

## Project Structure

```text
stock_market_predictor
 ├── stock_prediction.py     → Primary application server, model parsing, and chart outputs
 ├── index.html              → Display markup variables defining presentation constraints
 ├── static/
 │   └── {TICKER}_graph.png  → Target destination directory caching graphical plotting instances
 ├── {TICKER}_prediction.pkl → Active stored models mapped via string designations
 └── README.md
```

<br>

## Built With

| Technology | Purpose |
|---|---|
| **Python** | Central application configuration and runtime |
| **Flask** | Gateway network framework instances |
| **scikit-learn** | Predictive ML architectural bounds |
| **yfinance** | Baseline real-time mapping engine |
| **Pandas / NumPy** | Mathematical logic rendering schemas |
| **Matplotlib** | Visual charting structure logic |
| **joblib** | Process management optimization arrays |

<br>

## Disclaimer

> This project is defined as an **educational structural machine learning demo implementation**. It holds natural inherent variance structures characteristic of algorithmic models. Standard predictive results should **never** directly orient definitive real-world financial commitments. Leverage accredited advisory networks prior to financial actions.

<br>

## Contributing

Process alterations mapping functional implementations are naturally welcome for iterative versions.

```bash
git checkout -b feature/lstm-model
git commit -m "Initialize recurrent memory sequence mapping options"
git push origin feature/lstm-model
```

<br>
