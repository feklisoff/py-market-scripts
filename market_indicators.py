import requests
import os
from dotenv import load_dotenv
load_dotenv()

ALPHAVANTAGE_APIKEY = os.environ.get('ALPHA_V_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query?'


# This API returns the monthly Advance Retail Sales: Retail Trade data of the United States, outputs monthly data since 1992 Jan 1st
def get_all_monthly_retail_sales():
    url = BASE_URL + 'function=RETAIL_SALES&apikey=' + ALPHAVANTAGE_APIKEY
    r = requests.get(url)
    data = r.json()

    print(data)

# This API returns the annual and quarterly Real GDP of the United States.
def get_all_real_gdp(interval='annual'):
    #interval can be either 'annual' or 'quarterly'
    url = BASE_URL + 'function=REAL_GDP&interval=' + interval + '&apikey=' + ALPHAVANTAGE_APIKEY
    r = requests.get(url)
    data = r.json()

    print(data)

# This API returns the annual inflation rates (consumer prices) of the United States, outputs annual data since 1960 Jan 1st
def get_all_annual_inflation():
    url = BASE_URL + 'function=INFLATION&apikey=' + ALPHAVANTAGE_APIKEY
    r = requests.get(url)
    data = r.json()

    print(data)

# This API returns the monthly inflation expectation data of the United States, as measured by the median expected price change next 12 months 
# according to the Surveys of Consumers by University of Michigan (Inflation Expectation© [MICH]), retrieved from FRED, Federal Reserve Bank of St. Louis.
def get_all_inflation_expectation():
    url = BASE_URL + 'function=INFLATION_EXPECTATION&apikey=' + ALPHAVANTAGE_APIKEY
    r = requests.get(url)
    data = r.json()

    print(data)

def get_all_monthly_consumer_sentiment():
    url = BASE_URL + 'function=CONSUMER_SNETIMENT&apikey=' + ALPHAVANTAGE_APIKEY
    r = requests.get(url)
    data = r.json()

    print(data)

def get_all_monthly_unemployment():
    url = BASE_URL + 'function=UNEMPLOYMENT&apikey=' + ALPHAVANTAGE_APIKEY
    r = requests.get(url)
    data = r.json()

    print(data)