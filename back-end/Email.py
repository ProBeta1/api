import random
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# message = Mail(
#     from_email='gdbextraemail@gmail.com',
#     to_emails='gdbextraemail@gmail.com',
#     subject='testing mail',
#     html_content='<strong>Testing API</strong>'
# )
# print(os.environ.get('SENDGRID_API_KEY'))
# try:
#     sg=SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
#     response=sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.header)
# except Exception as e:
#     print(e)



class TwilioSend:
    # email in constructor indicates email of recipient
    def __init__(self, reemail):
        self.reemail = reemail
    def send_message(self, em_message):
        message = Mail(
            from_email='gdbextraemail@gmail.com',
            to_emails=self.reemail,
            subject='Thank you for the treat',
            html_content=em_message
        ) 
        try:
            sg=SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response=sg.send(message)
            print(response.status_code)
            print(response.body)
            # print(response.header)
            return 1
        except Exception as e:      
            print(e)
            return -1







# function email_otp will contain the code to email the OTP
class Email:
    def __init__(self, email):
        self.email = email
    def generate_otp(self):
        self.otp = str(random.randint(111111, 999999))
        email_send_check = self.email_otp()
        if email_send_check == -1:
            print("Email send fail")
            return -1
        else:
            print("email send pass")
            return self.otp
    def email_otp(self):
        # Implement Twilio Code to send OTP here
        otp_send_obj = TwilioSend(self.email)
        opt_send_resp = otp_send_obj.send_message(self.otp)
        # otp sent successfully
        if opt_send_resp == 1:
            return 1
        else:
            return -1
