import os 
from sendgrid import SendGridAPIClient 
from sendgrid.helpers.mail import Mail

def request_notification(emails, campaign_name):
    message = Mail(
        from_email = 'ethoboost@gmail.com',
        to_emails=emails, 
        subject='Ethoboost Campaign Request',
        html_content=( f'<h4>There is a new request for {campaign_name}</h4>'
                        '<p>To vote please go to the Etho-Boost homepage: <a href = https://etho-boost-crowdfund.herokuapp.com/ > Click Here </a></p>'
                        f"<ul><li>Click on 'My Boosters' in the nav bar</li><li>Click on the 'Contributor' panel</li><li>In the {campaign_name} section, vote on the open request</li></ul>" ) 
    )
    try: 
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e: 
        print(e.message)