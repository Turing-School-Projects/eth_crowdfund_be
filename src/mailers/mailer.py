import os 
from sendgrid import SendGridAPIClient 
from sendgrid.helpers.mail import Mail

def request_notification(emails, request_link):
    message = Mail(
        from_email = 'ethoboost@gmail.com',
        to_emails=emails, 
        subject='Ethoboost Campaign Request',
        html_content=f'There is a new request that requires your vote: {request_link}'
    )
    try: 
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        sg.send(message)
    except Exception as e: 
        print(e.message)