from flask import Flask
from flask import request
from twilio.rest import Client
from marketstack import get_stock_price
import os
app = Flask(__name__)

#ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
ACCOUNT_ID = "AC3056e8e41c6d7e505164d8fef4a2449b"
#TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_TOKEN = "7386ca6fe86d4a424558e2c65b30bc71"
client = Client(ACCOUNT_ID,TWILIO_TOKEN)
TWILIO_NUMBER = 'whatsapp:+14155238886'

def send_msg(msg,recipient):
    client.messages.create(
    from=TWILIO_NUMBER,
    body=msg,
    to=recipient
    )

def process_msg(msg):
response = ""
if msg == "hi":
response = "Hello,welcome to the stock market bot!"
response += "Type sym:<stock_symbol> to know the price of stock."
elif 'sym' in msg:
    data = msg.split(":")
    stock_symbol = data[1]
    stock_price = get_stock_price(stock_symbol)
    last_price = stock_price['last_price']
    last_price_str = str(last_price)
    response = "The stock price of " + stock_symbol + "is: $" + last_price_str
else:
    response = "Please type hi to get started."
return response 

@app.route("/webhook",methods=["POST"])
def webhook():
f = request.form
msg = f['Body']
sender = f['From']
response = process_msg(msg)
send_msg(response,sender)
return "OK",200