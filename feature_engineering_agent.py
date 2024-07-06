class FeatureEngineeringAgent:
    def create_features(self, data):
        data['MA20'] = data['Close'].rolling(window=20).mean()
        data['MA50'] = data['Close'].rolling(window=50).mean()
        data['Lag1'] = data['Close'].shift(1)
        data['Lag2'] = data['Close'].shift(2)
        return data.dropna()