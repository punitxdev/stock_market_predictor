# 📈 Stock Market Predictor

A modern, AI-powered stock prediction web application built with Python (Flask) and a beautiful HTML/CSS frontend. It utilizes a custom Linear Regression model engine to forecast stock valuations over the next 1-30 days based on historical data.

## ✨ Features
* **Custom AI Engine:** Uses a tailored `LinearRegression` model trained specifically on historical Close prices fetched dynamically via `yfinance`.
* **Stunning UI:** A responsive, glassmorphic UI featuring dark mode, animated gradient text, and dynamic background blobs.
* **Smart Loading States:** Automatically checks if a model exists for your specific stock ticker and elegantly switches loading states between "Loading the model..." and "Predicting...".
* **Side-by-Side Results:** Smooth, real-time forecast table placed adjacent to the input form with custom scrollbars to prevent page stretching.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3 installed. Navigate to the project folder and install the required dependencies:
```bash
pip install -r requirements.txt
```
*(If you are missing `flask` or `flask-cors`, install them via `pip install flask flask-cors`)*

### Running the App
Start the Flask server by running the main Python script:
```bash
python3 stock_prediction.py
```
The server will start on `http://127.0.0.1:5000` and automatically pop open in your default web browser!

## 🛠️ How it Works
1. Enter any valid Yahoo Finance stock ticker (e.g., `AAPL`, `TSLA`, `NVDA`).
2. Input how many business days into the future you'd like to predict.
3. Once you hit predict, the backend will verify if a `.pkl` model already exists for that stock. If not, it fetches real-time data, trains a fresh LinearRegression model, and saves it.
4. The system calculates the predicted values and calculates trend direction based on the current close price.

## 📄 Repository Structure
- `stock_prediction.py` - The core AI model logic and Flask API server bundled together.
- `index.html` - The frontend UI, directly loaded by Flask from the root directory.
- `requirements.txt` - Required Python packages.
