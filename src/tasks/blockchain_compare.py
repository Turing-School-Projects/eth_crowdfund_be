import time 
from src.models.Campaign import Campaign

# def example(seconds): 
#     print('Starting task')
#     for i in range(seconds): 
#         print(i)
#         time.sleep(1)
#     print('Task Complete')

def compare_campaign_value(): 
    updated_databases = []
    # Get all campaign addresses 
    campaigns = Campaign.get_all_campaigns
    # Query blockchain for each campaign 
    for campaign in campaigns: 
        query_blockchain(address)
        # Convert blockchain value if needed
        convert_wei_to_eth
        # Compare blockchain value with DB value
        if block_value != campaign.value: 
            camapign.update({'value': block_value})
            updated_databases.append(campaign.id)