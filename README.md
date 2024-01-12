# Stock chatbot
• Implemented a System that gives you update for current marketprice of any stock through chat.
• Retrieved data from MarketStack API, having the key to accessing real-time stock market data. It empowers the bot with up-to-date information for accurate stock price.
• Implemented using Python having rich set of libraries make it ideal for data analysis and automation.
• Twilio is the communication platform that enables the bot to send stock market updates and notification to users via Whatsapp. It provides an intuitive and reliable messaging API.
• The reason for using Whatsapp other than any social media platform:
  1. Having more than 2 Billion User base.
  2. Most popular messaging app & easy to use.
  3. Provide end to end encryption for security.
  4. Easy to integrate for Developers.
• How does it actually works, let's see step by step:
  1. User sends a message to the twilio provided sandbox account.
  2. Twilio receeives the message, calls the registered webhooks and sends data
  3. Flask app receives the request, parse the request and get the stock data from marketstack
  4. Marketstack API returns the stock price data

 
