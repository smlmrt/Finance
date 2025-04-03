Stock Price Prediction with LSTM
This project demonstrates how to predict the stock price of a company using the LSTM (Long Short-Term Memory) model, a type of recurrent neural network. The model predicts the next day's closing price based on historical stock data.

Libraries Used
yfinance: Used to download stock data from Yahoo Finance.

pandas: Data manipulation and preparation.

numpy: Used for numerical operations and array manipulations.

sklearn: Data scaling using MinMaxScaler.

tensorflow.keras: LSTM model construction and training.

Installation
Install the required libraries using pip:

bash
Kopyala
Düzenle
pip install yfinance pandas numpy scikit-learn tensorflow
How to Run
Run the Python script from the terminal or command line:

bash
Kopyala
Düzenle
python stock_price_prediction.py
Code Explanation
Stock Data Download:

The script fetches stock data for a given ticker symbol (e.g., THYAO.IS) from Yahoo Finance. If the primary ticker fails, it tries alternative tickers (e.g., THYAO, THYAO.BIST).

Data Preprocessing:

The missing values in the data are filled using the forward fill method.

The closing prices are extracted and scaled to a range between 0 and 1 using MinMaxScaler.

Data Preparation for LSTM:

The data is prepared for LSTM by creating sequences of 60 previous days' closing prices to predict the next day's closing price.

Model Construction:

An LSTM model is created with two LSTM layers and one Dense output layer.

The model is compiled using the Adam optimizer and mean squared error loss.

Model Training:

The model is trained on the data for 10 epochs with a batch size of 32.

Prediction:

The script uses the last 60 days of stock data to predict the next day's closing price.

The predicted price is then scaled back to the original range (using inverse transformation).

Output
The predicted closing price for the next day is printed in Turkish Lira (TL).

Example Output:
Kopyala
Düzenle
📊 Bir sonraki günün tahmini kapanış fiyatı: 150.23 TL
Customization
Ticker Symbol: You can modify the script to use different ticker symbols for other stocks. Just change the value of alternative_tickers or pass a different ticker to the get_stock_data function.

Sequence Length: You can change the sequence length (sequence_length = 60) to use a different number of previous days for prediction.

Epochs and Batch Size: You can adjust the number of epochs and batch size based on your system and dataset size.
