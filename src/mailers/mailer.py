from flask_mail import Message
from ..app import mail 


# Takes in an array of email addresses and the url to the request to be voted on 
def request_notification(emails, request_link):
    with mail.connect() as conn: 
        for email in emails: 
            message = f"There is a new request: {request_link}"
            subject = "Ethoboost Campaign Request"
            msg = Message(recipients=[email],
                        body=message,
                        sender="noreply@ethoboost.com",
                        subject=subject)
            conn.send(msg)

