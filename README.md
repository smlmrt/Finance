# 📈 LSTM Stock Price Prediction

This project uses a Long Short-Term Memory (LSTM) neural network to predict stock prices based on historical data. The implementation focuses on predicting the next day's closing price for Turkish Airlines (THYAO) stock using the previous 60 days of trading data.

## ✨ Features

- 🔄 Downloads historical stock data using Yahoo Finance API
- 🧹 Handles missing values and performs data preprocessing
- 📊 Scales data for optimal neural network performance
- 🧠 Implements LSTM architecture for time series forecasting
- 🔮 Predicts the next day's closing price

## 🛠️ Technologies & Libraries

- **Python 3.x**
- **TensorFlow/Keras**: For building and training the LSTM model
- **yfinance**: For downloading stock data from Yahoo Finance
- **pandas**: For data manipulation and preprocessing
- **numpy**: For numerical operations
- **scikit-learn**: For data scaling using MinMaxScaler

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/lstm-stock-prediction.git
cd lstm-stock-prediction
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install yfinance pandas numpy scikit-learn tensorflow
```

## 🚀 Usage

Run the main script to fetch data, train the model, and predict the next day's stock price:

```bash
python stock_price_prediction.py
```

By default, the script will:
1. Download historical data for Turkish Airlines (THYAO) from Yahoo Finance
2. Preprocess and scale the data
3. Create and train an LSTM model on the historical closing prices
4. Predict the next day's closing price

## 🔍 How It Works

### Data Collection
- The script fetches stock data from Yahoo Finance using the `yfinance` library
- It tries different ticker symbols (THYAO.IS, THYAO, THYAO.BIST) to ensure data availability

### Data Preprocessing
- Missing values are filled using the forward fill method
- The closing prices are extracted and scaled to a range between 0 and 1 using MinMaxScaler

### LSTM Model
- Sequences of 60 previous days' closing prices are created as input features
- A two-layer LSTM model is constructed with 50 units in each layer
- The model is trained to predict the next day's closing price

### Prediction
- The model uses the last 60 days of scaled data to predict the next day's price
- The prediction is inverse-transformed to get the actual price value

## 🔄 Extending the Project

To use this model with different stocks:
- Change the ticker symbols in the `alternative_tickers` list
- Adjust the `sequence_length` variable if you want to use a different time window
- Modify the LSTM architecture or training parameters for potentially better results

## 📊 Sample Output

```
Veri çekiliyor: THYAO.IS...
✅ Veri başarıyla alındı: THYAO.IS
[...]
📊 Bir sonraki günün tahmini kapanış fiyatı: XX.XX TL
```

## ⚠️ Limitations

- Stock price prediction is inherently challenging due to market volatility
- The model only considers historical prices and doesn't factor in news, events, or other external factors
- Performance may vary depending on market conditions and the specific stock

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
