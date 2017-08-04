import json
import time
import hashlib
import hmac
import base64
import random
import datetime
import httplib
import urllib
import urllib2

#made by Colin Daly
#never used python before no h8

#TODO track the count so we don't get banned

class kraken:
	def __init__(self, version = '0', APIKey = '', Secret = '', timeout = 10, uri = 'https://api.kraken.com'):
		self.APIKey = APIKey
		self.Secret = Secret
		self.ApiVersion = version
		self.uri = uri

	def close(self):
		self.connection.close()
		
	def load_key(self, path = '.apis'):

		with open(path, 'r') as file:
			data = json.load(file)
			self.APIKey = data["apis"][0]["apikey"]
			self.Secret = data["apis"][0]["secret"]
		return

	def query_private(self, method, req=None):
		if (req==None):
			req = {}

		urlstring = '/' + self.ApiVersion + '/private/' + method
		req['nonce'] = int(1000*time.time())
		post = urllib.urlencode(req)
		encoded = (str(req['nonce']) + post).encode()
		message = urlstring + hashlib.sha256(str(req['nonce']) + post).digest()

		signature = hmac.new(base64.b64decode(self.Secret), message, hashlib.sha512)

		headers = {
			'API-Key': self.APIKey,
			'API-Sign':base64.b64encode(signature.digest())
				}
		

		ret = urllib2.urlopen(urllib2.Request((self.uri+urlstring), post, headers))
		return json.loads(ret.read())

	def query_public(self, method, req=None):
		if (req==None):
			req = {}
		urlstring = '/' + self.ApiVersion + '/public/' + method
		post = urllib.urlencode(req)
		headers = {}
		ret = urllib2.urlopen(urllib2.Request((self.uri+urlstring), post, headers))
		return json.loads(ret.read())

	def getAssetInfo(self, assets=None):
		req = {}
		if (assets!=None):
			req['asset'] = assets
		#returns array of asset names with info:
			#<asset_name> = asset name
		    #altname = alternate name
		    #aclass = asset class
		    #decimals = scaling decimal places for record keeping
		    #display_decimals = scaling decimal places for output display
		return self.query_public("Assets", req)

	def getAssetPairs(self, pair = None):
		req = {}
		if (pair!=None):
			req['pair'] = pair
		return self.query_public("AssetPairs")

	def getTickerInfo(self, pair):
		req = {}
		req['pair'] = pair
		return self.query_public("Ticker", req)

	def getAccountBalance(self):
		return self.query_private("Balance")

	def getOpenOrders(sel):
		return self.query_private("OpenOrders")

	def order(self, pair, type, ordertype, volume, price = None, price2 = None, starttm = None, expiretm = None):
		req = {}
		req['pair'] = pair
		req['type'] = type
		req['ordertype'] = ordertype
		req['volume'] = volume
		req['price'] = price
		req['price2'] = price2
		req['starttm'] = starttm
		req['expiretm'] = expiretm

		return self.query_private("AddOrder", req)
	

	#buy some coin from USD
	def limitBuy(self, pair, price, volume):
		return self.order(pair, "buy", "limit", volume, price, price, 0, 0)

	def marketBuy(self, pair, volume):
		return self.order(pair, "buy", "market", volume, price, price, 0, 0)
	

	#buy some coin from USD
	#don't forget to sell high
	def limitSell(self, pair, price, volume):
		return self.order(pair, "sell", "limit", volume, price, price, 0, 0)

	def marketSell(self, pair, volume):
		return self.order(pair, "sell", "market", volume, 10000, 10000, 0, 0)
		#fix this


	def cancelOrder(self, txid):
		eq['txid'] = txid
		return self.query_private("CancelOrder", req)

		