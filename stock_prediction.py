from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
import os
import threading
import webbrowser

# Tell Flask to look for HTML files in the SAME directory! This keeps all files in one place.
app = Flask(__name__, template_folder='.')

@app.route("/")
def home():
    # Looks for index.html in the same directory, no 'templates' folder needed
    return render_template("index.html")

@app.route("/check_model", methods=["POST"])
def check_model():
    data = request.json
    stock = data.get("stock", "AAPL").upper()
    model_file = f"{stock}_prediction.pkl"
    return jsonify({"exists": os.path.exists(model_file)})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    stock = data.get("stock", "AAPL").upper()
    future_days = int(data.get("future_days", 1))
    model_file = f"{stock}_prediction.pkl"
    
    try:
        raw_data = yf.download(stock, start="2000-01-01", end="2026-01-01", progress=False)
        
        if raw_data.empty:
            return jsonify({"error": f"No data found for ticker '{stock}'."}), 400
            
        df = pd.DataFrame(raw_data)
        df = df[['Close']]
        df['Prediction'] = df['Close'].shift(-future_days)
        
        X = np.array(df.drop(['Prediction'], axis=1))[:-future_days]
        y = np.array(df['Prediction'])[:-future_days]
        
        if os.path.exists(model_file):
            model = joblib.load(model_file)
        else:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            model = LinearRegression()
            model.fit(X_train, y_train)
            joblib.dump(model, model_file)
            
        X_future = np.array(df.drop(['Prediction'], axis=1))[-future_days:]
        pred = model.predict(X_future)
        
        current_price = float(np.ravel(df['Close'].values[-1])[0])
        current_date = df.index[-1].strftime("%Y-%m-%d")
        
        predictions = []
        for p in pred:
            val = float(np.ravel(p)[0])
            predictions.append(val)
            
        return jsonify({
            "ticker": stock,
            "current_price": current_price,
            "current_date": current_date,
            "predictions": predictions
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Initializing stock Predict Engine...")
    print("Opening browser automatically...")
    threading.Timer(1.5, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=True, port=5000, use_reloader=False)