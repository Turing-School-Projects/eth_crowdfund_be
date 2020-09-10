import os 
from sendgrid import SendGridAPIClient 
from sendgrid.helpers.mail import Mail

def request_notification(emails, request_link):
    message = Mail(
        from_email = 'ethoboost@gmail.com',
        to_emails=emails, 
        subject='Ethoboost Campaign Request',
        html_content=f'there is a new request: {request_link}'
    )
    try: 
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e: 
        print(e.message)