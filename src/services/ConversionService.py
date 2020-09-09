from flask import Response, Request
import requests

class ConversionService:
    def __init__(self): 
        self.url = 'https://min-api.cryptocompare.com/data/price'

    def wei_to_usd(self, wei):
        eth_amount = self.wei_to_eth(wei)
        return self.eth_to_usd(eth_amount)

    def eth_to_usd(self, eth): 
        query_params = { 'fsym':'ETH' , 'tsyms':'USD'}
        response = requests.get(self.url, params=query_params)
        conversion_rate = response.json()['USD'] 
        return eth * conversion_rate

    def wei_to_eth(self, wei):
        return wei * pow(10, -18)

    