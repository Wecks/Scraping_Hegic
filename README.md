# What do I do here ?
The purpose of this code is to scrape data from the [Hegic website](https://www.hegic.co/app#/arbitrum/trade/new) and extract option premiums that I am interested in. 

Here's what the code does: 
- Retrieves the premium from Hegic
- Retrieves the asset price from the Binance API
- Stores the data in an Excel file that I have created
- Repeats this process every 8 hours

# Why am I doing this ?
I am experimenting with a trading strategy that revolves around options and is based on the volatility of the BTC and ETH market. 

Specifically, I am using a strategy called "Straddle". 

The goal is to purchase the option when its price is low, indicating low volatility. I anticipate that the volatility will increase in the near future, leading to price movement in either direction, thus allowing me to profit from my option strategy.

## Credits and Author
Wecks