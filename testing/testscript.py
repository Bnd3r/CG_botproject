import krakenex
import time

ap = 'XETHZEUR'
k  = krakenex.API() # Public Kraken API call

# Get local time
print(k.query_public('Time')['result']['rfc1123'])

# Display assets
def print_method(param_method):
   """ Print public methods
   :param method: API method name
   """
   q_assets = k.query_public(param_method)
   assets = q_assets['result']

   for key, value in assets.items() :
	    print (key)


# print(k.query_public('AssetPairs',{'info' : 'info', 'pair' : 'XETHZEUR, XXBTZEUR'}))
# Display asset pairs
# XETHZEUR
# XXBTZEUR
current_price = float(k.query_public('Ticker',{'pair' : 'XETHZEUR'})['result']['XETHZEUR']['c'][0])

while True:        # Loop until it is a blank line
	new_price = float(k.query_public('Ticker',{'pair' : 'XETHZEUR'})['result']['XETHZEUR']['c'][0])
	if (new_price/current_price - 1.0 > 0.001):
		print(new_price, current_price, 'sell')

	print(k.query_public('Time')['result']['rfc1123'], k.query_public('Ticker',{'pair' : 'XETHZEUR'})['result']['XETHZEUR']['c'][0])
	time.sleep(600)
print('end')