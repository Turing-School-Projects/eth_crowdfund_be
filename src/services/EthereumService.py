import os 
from web3 import Web3 


class EthereumService:

    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(f'https://rinkeby.infura.io/v3/${os.getenv('INFURA_API_KEY')}')

    def get_campaign_value(campaign_address):
        import pdb; pdb.set_trace
        wei_balance = w3.eth.getBalance(campaign_address)