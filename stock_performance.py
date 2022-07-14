import requests
import os
from dotenv import load_dotenv
load_dotenv()

ALPHAVANTAGE_APIKEY = os.environ.get('ALPHA_V_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query?function='

available_functions = {'weekly': 'TIME_SERIES_WEEKLY', 'monthly': 'TIME_SERIES_MONTHLY'}

market_indices = [
    'SPX', 'DJIA', 'COMP'
]
high_valuation_stocks = [
    'AAPL', 'AMZN', 'META', 'MSFT', 'GOOGL'
]

# sample_url = BASE_URL + available_functions.get(weekly) + '&symbol=' + market_indices[0]