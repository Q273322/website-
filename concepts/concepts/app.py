from flask import Flask, render_template, jsonify
import pandas as pd
from data_handler import fetch_data
from strategies import execute_strategy

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch market data for a single pair
    pair = 'EUR/USD'
    all_data = fetch_data([pair])
    data = all_data[pair]

    # Execute trading strategy and generate signals
    signals = execute_strategy(data)  # Assuming execute_strategy returns signals

    # Prepare data for the web page and include historical signals
    trading_info = []
    historical_signals = []  # Placeholder for historical signals logic

    if signals:
        signal = signals[0]  # Get only the first signal
        reason = 'Price action indicates a buying opportunity.' if signal['signal'] == 'buy' else 'Price action indicates a selling opportunity.'
        trading_info.append({
            'pair': pair,
            'signal': signal['signal'],
            'current_price': signal['price'],
            'reason': reason,
            'tp': signal['price'] * 1.02 if signal['signal'] == 'buy' else signal['price'] * 0.98,
            'sl': signal['price'] * 0.98 if signal['signal'] == 'buy' else signal['price'] * 1.02
        })

        # Add to historical signals
        historical_signals.append({
            'pair': pair,
            'signal': signal['signal'],
            'current_price': signal['price'],
            'reason': reason,
            'tp': signal['price'] * 1.02 if signal['signal'] == 'buy' else signal['price'] * 0.98,
            'sl': signal['price'] * 0.98 if signal['signal'] == 'buy' else signal['price'] * 1.02
        })

    return render_template('index.html', trading_info=trading_info, historical_signals=historical_signals)

@app.route('/signals')
def signals():
    # Fetch market data for a single pair
    pair = 'EUR/USD'
    all_data = fetch_data([pair])
    data = all_data[pair]

    # Execute trading strategy and generate signals
    signals = execute_strategy(data)  # Assuming execute_strategy returns signals

    # Prepare only the first signal for JSON response
    signal_data = []
    if signals:
        signal = signals[0]  # Get only the first signal
        reason = 'Price action indicates a buying opportunity.' if signal['signal'] == 'buy' else 'Price action indicates a selling opportunity.'
        signal_data.append({
            'pair': pair,
            'signal': signal['signal'],
            'current_price': signal['price'],
            'reason': reason,
            'tp': signal['price'] * 1.02 if signal['signal'] == 'buy' else signal['price'] * 0.98,
            'sl': signal['price'] * 0.98 if signal['signal'] == 'buy' else signal['price'] * 1.02
        })

    return jsonify(signal_data)

if __name__ == "__main__":
    app.run(debug=True)
