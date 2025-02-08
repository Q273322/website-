import ccxt
import pandas as pd
def fetch_data(pairs=['EUR/USD'], timeframe='15m', limit=100):
    # Initialize the exchange
    exchange = ccxt.kraken()
    all_data = {}

    for pair in pairs:
        # Fetch historical data for each trading pair
        ohlcv = exchange.fetch_ohlcv(pair, timeframe, limit=limit)
        
        # Convert to DataFrame
        data = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
        
        # Store data in a dictionary
        all_data[pair] = data

    return all_data
