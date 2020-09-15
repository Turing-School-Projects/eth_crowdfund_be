import os 
from web3 import Web3 


class EthereumService:

    def __init__(self):
        key = os.getenv('INFURA_API_KEY')
        self.w3 = Web3(Web3.HTTPProvider(f"https://rinkeby.infura.io/v3/{key}"))


    def get_campaign_value(self, campaign_address):
        try: 
            wei_balance = self.w3.eth.getBalance(campaign_address)
            return wei_balance
        except: 
            return 'error'