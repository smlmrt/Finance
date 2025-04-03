import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Tarih aralığını belirle
end_date = datetime.today()
start_date = datetime(2000, 12, 26)

# Hisse senedi verisini çekme fonksiyonu
def get_stock_data(ticker):
    try:
        print(f"Veri çekiliyor: {ticker}...")
        data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
        
        if data.empty:
            print(f"⚠️ Veri çekilemedi: {ticker}")
            return None
        
        print(f"✅ Veri başarıyla alındı: {ticker}")
        return data
    except Exception as e:
        print(f"❌ Hata oluştu ({ticker}): {e}")
        return None

# Alternatif ticker kodlarını dene
alternative_tickers = ["THYAO.IS", "THYAO", "THYAO.BIST"]
data = None

for ticker in alternative_tickers:
    data = get_stock_data(ticker)
    if data is not None:
        break  # Çalışan bir ticker bulunursa döngüyü durdur

# Eğer hiçbir ticker ile veri çekilemezse hata ver
if data is None:
    raise ValueError("Hisse senedi verisi çekilemedi. Alternatif kaynakları deneyin.")

# Eksik değerleri doldurma
data.fillna(method='ffill', inplace=True)

# Kapanış fiyatını kullanarak modelleme yapacağız
closing_prices = data['Close'].values.reshape(-1, 1)

# Veriyi ölçeklendirme (MinMaxScaler ile 0-1 arasında ölçeklendirme)
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(closing_prices)

# Eğitim verisi oluşturma (LSTM için veri setinin hazırlanması)
train_data, labels = [], []
sequence_length = 60  # Son 60 günü kullanarak bir sonraki günü tahmin edeceğiz

for i in range(sequence_length, len(scaled_data)):
    train_data.append(scaled_data[i-sequence_length:i, 0])
    labels.append(scaled_data[i, 0])

train_data, labels = np.array(train_data), np.array(labels)
train_data = np.reshape(train_data, (train_data.shape[0], train_data.shape[1], 1))

# LSTM modeli oluşturma
model = Sequential([
    LSTM(units=50, return_sequences=True, input_shape=(train_data.shape[1], 1)),
    LSTM(units=50),
    Dense(units=1)
])

# Modeli derleme
model.compile(optimizer='adam', loss='mean_squared_error')

# Modeli eğitme
model.fit(train_data, labels, epochs=10, batch_size=32)

# Test verisi hazırlama (bir sonraki günü tahmin etmek için son 60 veriyi kullanacağız)
last_60_days = scaled_data[-60:]
last_60_days_scaled = last_60_days.reshape(1, last_60_days.shape[0], 1)

# Bir sonraki günün tahminini yapma
predicted_price = model.predict(last_60_days_scaled)
predicted_price = scaler.inverse_transform(predicted_price)

print(f"📊 Bir sonraki günün tahmini kapanış fiyatı: {predicted_price[0][0]:.2f} TL")
