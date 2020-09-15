from src.models.Campaign import Campaign
from src.services.EthereumService import EthereumService
from src.services.ConversionService import ConversionService
# from src.app import create_app
import os
import time


def compare_campaign_value():
    from src.app import create_app
    env_name = os.getenv('FLASK_ENV') 
    app = create_app(env_name)
    app.app_context().push()

    ethereum_service = EthereumService()
    conversion_service = ConversionService()
    updated_databases = []
    # Get all campaign addresses 
    campaigns = Campaign.get_all_campaigns()
    # Query blockchain for each campaign 
    for campaign in campaigns: 
        print(campaign)
        time.sleep(2) 
        campaign_value_wei_bc = ethereum_service.get_campaign_value(campaign.address)
        if campaign_value_wei_bc == 'error':
            continue
        # Convert blockchain value if needed
        campaign_value_eth_bc = conversion_service.wei_to_eth(campaign_value_wei_bc)
        # Compare blockchain value with DB value
        if campaign_value_eth_bc != campaign.value: 
            campaign.update({'value': campaign_value_eth_bc})
            updated_databases.append(campaign.id)
    
    return print("hello world")