import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='gdbextraemail@gmail.com',
    to_emails='gdbextraemail@gmail.com',
    subject='testing mail',
    html_content='<strong>Testing API</strong>'
)
print(os.environ.get('SENDGRID_API_KEY'))
try:
    sg=SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response=sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.header)
except Exception as e:
    print(e)