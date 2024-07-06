import yfinance as yf

class DataCollectionAgent:
    def collect_data(self, ticker, start_date, end_date):
        data = yf.download(ticker, start=start_date, end=end_date)
        return data