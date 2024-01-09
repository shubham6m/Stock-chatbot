#save this file with name marketstack.py

#MARKETSTACK_KEY

#0 explore the marketstack docs & find the relevent url
#1 integrate api

#import 
import os
import requests
import json

API_KEY  = "20b1f217d81dd9c5873cdc04968a0d1f"
BASE_URL = 'https://api.marketstack.com/v1/'

def get_stock_price(stock_symbol):
    params = {
        'access_key': API_KEY
    }
    end_point = ''.join([BASE_URL,"tickers/",stock_symbol,"/intraday/latest"])
    api_result = requests.get(end_point, params)
    print(api_result)
    json_result = json.loads(api_result.text)
    return{
        "last_price": json_result["last"]
    }
result = get_stock_price("AAPL")
print(result)