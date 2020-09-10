# from flask_mail import Message
# from ..app import mail 
import os 
from sendgrid import SendGridAPIClient 
from sendgrid.helpers.mail import Mail


# # Takes in an array of email addresses and the url to the request to be voted on 
# def request_notification(emails, request_link):
#     with mail.connect() as conn: 
#         for email in emails: 
#             message = f"There is a new request: {request_link}"
#             subject = "Ethoboost Campaign Request"
#             msg = Message(recipients=[email],
#                         body=message,
#                         sender="noreply@ethoboost.com",
#                         subject=subject)
#             conn.send(msg)

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